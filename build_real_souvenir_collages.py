import urllib.request
import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import io

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

raw_dir = Path("images/real_raw")
raw_dir.mkdir(parents=True, exist_ok=True)
out_dir = Path("images")

def download_image(url, filename):
    filepath = raw_dir / filename
    if filepath.exists() and filepath.stat().st_size > 1000:
        print(f"Already downloaded: {filename}")
        return filepath
    print(f"Downloading {filename} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req, timeout=15).read()
        with open(filepath, 'wb') as f:
            f.write(data)
        print(f"Saved {filename} ({len(data)} bytes)")
        return filepath
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
        return None

# Real Product Image URLs
products = {
    # Czech
    "czech_kohinoor": "http://artshop.com.tw/image/catalog/KOH-I-NOOR/K3405.jpg",
    "czech_botanicus": "https://cdn11.bigcommerce.com/s-wy24pmvooy/images/stencil/1280x1280/products/391/1135/Special_soap_with_Dead_Sea_mud_1__42279.1637467812.jpg",
    "czech_manufaktura": "https://manufakturashop.com/data/tmp/26/1/9071_26.en.jpg",
    "czech_kolonada": "https://www.aeliadutyfree.cz/media/catalog/product/1/0/100344061_1_2d68.jpg",
    
    # Austria
    "austria_fuerst": "https://upload.wikimedia.org/wikipedia/commons/8/87/Box_of_Original_Mozart_Kugeln_F%C3%BCrst.jpg",
    "austria_mirabell": "https://m.media-amazon.com/images/I/91yWsZMQ-8L._SL1500_.jpg",
    "austria_manner": "https://upload.wikimedia.org/wikipedia/commons/0/00/2020-02-20-Manner_Neapolitane-Lokal_K-4775.jpg",
    "austria_salt": "https://shop.salzwelten.at/shop/Produktbilder/Speisesalz/Bad%20Ischler/Natursalz/image-thumb__2771__coreshop_productList/95220-bi-ns-streuer-glas-gemuese-garten-90g-3D-05.webp",
    
    # Germany
    "germany_knoppers": "https://americanuncle.es/cdn/shop/files/Knoppers-Minis-200g.png",
    "germany_toffifee": "https://static.vecteezy.com/system/resources/previews/054/315/032/non_2x/box-of-toffifee-candies-free-png.png",
    "germany_haribo": "https://assets.haribo.com/image/upload/s--I3hUAoXg--/ar_3225:4000,c_fill,f_auto,q_60/w_749/v1/consumer-sites/general/Saft-Golb%C3%A4ren_packshot_front.png",
    "germany_dallmayr": "https://www.coffeerista.com/media/da/ea/7d/1762178646/Dallmayr_prodomo_gemalen_voorkant.png",
    "germany_mivolis": "https://products.dm-static.com/images/f_auto,q_auto,c_fit,h_440,w_500/v1769553525/assets/pas/images/9ebf8098-6057-4c79-9d42-c7766435eaea/mivolis-multivitamin-brausetabletten-20-st",
    "germany_zwilling": "https://www.zwilling.com/dw/image/v2/BCGV_PRD/on/demandware.static/-/Sites-zwilling-master-catalog/default/dw2d86116e/images/large/4009839267758_02.jpg"
}

downloaded_files = {}
for name, url in products.items():
    fp = download_image(url, f"{name}.jpg")
    if fp and fp.exists():
        downloaded_files[name] = fp

print("\nDownloaded files count:", len(downloaded_files))

def create_card(img_path, label, target_size=(360, 360)):
    """Fit image into white card with label."""
    try:
        im = Image.open(img_path)
        im = ImageOps.exif_transpose(im)
        im = im.convert('RGB')
    except Exception as e:
        print(f"Error opening {img_path}: {e}")
        return None

    card = Image.new('RGB', (target_size[0], target_size[1] + 50), (255, 255, 255))
    
    # Calculate aspect ratio
    im.thumbnail((target_size[0] - 20, target_size[1] - 20), Image.Resampling.LANCZOS)
    x = (target_size[0] - im.width) // 2
    y = (target_size[1] - im.height) // 2
    card.paste(im, (x, y))
    
    draw = ImageDraw.Draw(card)
    # Border
    draw.rectangle([(0, 0), (card.width - 1, card.height - 1)], outline=(220, 224, 230), width=1)
    
    # Label bar
    draw.rectangle([(0, target_size[1]), (card.width, card.height)], fill=(245, 247, 250))
    draw.line([(0, target_size[1]), (card.width, target_size[1])], fill=(220, 224, 230), width=1)
    
    # Text
    try:
        font = ImageFont.truetype("msjh.ttc", 16) # Microsoft JhengHei
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), label, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (card.width - tw) // 2
    ty = target_size[1] + (50 - th) // 2
    draw.text((tx, ty), label, fill=(30, 41, 59), font=font)
    
    return card

def build_collage(items, output_path, cols=2):
    cards = []
    for key, label in items:
        if key in downloaded_files:
            c = create_card(downloaded_files[key], label)
            if c:
                cards.append(c)
    
    if not cards:
        print(f"No cards for {output_path}")
        return
        
    rows = (len(cards) + cols - 1) // cols
    cw, ch = cards[0].size
    margin = 16
    
    total_w = cols * cw + (cols + 1) * margin
    total_h = rows * ch + (rows + 1) * margin
    
    collage = Image.new('RGB', (total_w, total_h), (240, 243, 246))
    
    for idx, card in enumerate(cards):
        r = idx // cols
        c = idx % cols
        px = margin + c * (cw + margin)
        py = margin + r * (ch + margin)
        collage.paste(card, (px, py))
        
    collage.save(output_path, quality=92)
    print(f"Generated collage: {output_path} ({total_w}x{total_h})")

# 1. Czech collage
czech_items = [
    ("czech_botanicus", "菠丹妮 死海泥手工皂 (實品照)"),
    ("czech_manufaktura", "蔓菲蘿 啤酒花修護洗髮精 (實品照)"),
    ("czech_kohinoor", "Koh-i-Noor Magic 七彩魔術鉛筆 (實品照)"),
    ("czech_kolonada", "Kolonáda 傳統百年溫泉薄餅 (實品照)")
]
build_collage(czech_items, out_dir / "souvenirs_czech_real.jpg", cols=2)

# 2. Austria collage
austria_items = [
    ("austria_fuerst", "Fürst 原創手工莫札特巧克力 (銀藍版實品照)"),
    ("austria_mirabell", "Mirabell 超市版莫札特巧克力 (實品照)"),
    ("austria_manner", "Manner 經典榛果威化餅 (實品照)"),
    ("austria_salt", "Salzwelten 阿爾卑斯天然調味岩鹽 (實品照)")
]
build_collage(austria_items, out_dir / "souvenirs_austria_real.jpg", cols=2)

# 3. Germany collage
germany_items = [
    ("germany_knoppers", "Knoppers 牛奶榛果威化餅 (實品照)"),
    ("germany_toffifee", "Toffifee 太妃焦糖榛果夾心糖 (實品照)"),
    ("germany_haribo", "HARIBO Saft 真果汁小熊軟糖 (實品照)"),
    ("germany_dallmayr", "Dallmayr Prodomo 皇室咖啡 (實品照)"),
    ("germany_mivolis", "dm Mivolis 綜合發泡錠 (實品照)"),
    ("germany_zwilling", "雙人牌 TWINOX 超薄指甲剪 (實品照)")
]
build_collage(germany_items, out_dir / "souvenirs_germany_real.jpg", cols=3)

# 4. Copy raw Koh-i-noor to dedicated image
if "czech_kohinoor" in downloaded_files:
    Image.open(downloaded_files["czech_kohinoor"]).convert('RGB').save(out_dir / "kohinoor_real.jpg", quality=95)
    print("Saved kohinoor_real.jpg")
