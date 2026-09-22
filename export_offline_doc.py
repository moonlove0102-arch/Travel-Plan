import os
import re
import base64
from pathlib import Path
from markdown_it import MarkdownIt

def image_to_base64(img_path: Path) -> str:
    """Read an image file and convert it to a data URI."""
    suffix = img_path.suffix.lower().replace('.', '')
    mime = 'image/jpeg' if suffix in ['jpg', 'jpeg'] else f'image/{suffix}'
    with open(img_path, 'rb') as f:
        encoded = base64.b64encode(f.read()).decode('utf-8')
    return f'data:{mime};base64,{encoded}'

def get_processed_markdown(md_path: Path) -> str:
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    base_dir = md_path.parent

    def replace_img(match):
        alt = match.group(1)
        src = match.group(2)
        target_path = (base_dir / src).resolve()
        if target_path.exists() and target_path.is_file():
            data_uri = image_to_base64(target_path)
            return f'![{alt}]({data_uri})'
        return match.group(0)

    # Regex for ![alt](src)
    return re.sub(r'!\[(.*?)\]\((.*?)\)', replace_img, md_text)

def generate_booklet_html(md_file_path: str, output_html_path: str):
    """
    Generates a 2-up per A4 sheet booklet HTML:
    - Landscape A4 page setup (@page { size: A4 landscape; margin: 8mm 10mm; })
    - 2 balanced columns representing 2 pages per A4 sheet side-by-side
    - Middle dashed fold-line (column-rule) to easily fold into an A5 pocket booklet!
    """
    md_path = Path(md_file_path).resolve()
    processed_md = get_processed_markdown(md_path)
    md = MarkdownIt('commonmark').enable('table')
    body_html = md.render(processed_md)

    title = md_path.stem.replace('_', ' ').title()

    html_template = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>【A4雙頁小冊子版】{title}</title>
<style>
  :root {{
    --primary: #1e3a8a;
    --text: #1f2937;
    --bg: #f1f5f9;
    --card-bg: #ffffff;
    --border: #cbd5e1;
    --accent: #2563eb;
  }}
  * {{
    box-sizing: border-box;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Microsoft JhengHei", sans-serif;
    color: var(--text);
    background-color: var(--bg);
    margin: 0;
    padding: 16px;
    font-size: 13px;
    line-height: 1.5;
  }}

  /* Top bar for instructions */
  .toolbar {{
    max-width: 1280px;
    margin: 0 auto 16px auto;
    background: #1e293b;
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  }}
  .toolbar-title {{
    font-weight: 600;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .toolbar-hint {{
    font-size: 12px;
    color: #94a3b8;
  }}
  .print-btn {{
    background: #2563eb;
    color: white;
    border: none;
    padding: 8px 18px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
  }}
  .print-btn:hover {{
    background: #1d4ed8;
  }}

  /* Main Booklet Container */
  .booklet-container {{
    max-width: 1280px;
    margin: 0 auto;
    background: var(--card-bg);
    padding: 28px 36px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    column-count: 2;
    column-gap: 24mm;
    column-rule: 1px dashed #cbd5e1;
  }}

  h1 {{
    color: var(--primary);
    border-bottom: 2px solid var(--border);
    padding-bottom: 6px;
    margin-top: 0;
    font-size: 18px;
    break-after: avoid;
    page-break-after: avoid;
  }}
  h2 {{
    color: var(--primary);
    border-bottom: 1px solid var(--border);
    padding-bottom: 4px;
    margin-top: 20px;
    margin-bottom: 8px;
    font-size: 15px;
    break-after: avoid;
    page-break-after: avoid;
  }}
  h3, h4 {{
    color: #1e293b;
    margin-top: 14px;
    margin-bottom: 6px;
    font-size: 13.5px;
    break-after: avoid;
    page-break-after: avoid;
  }}
  p, ul, ol {{
    margin-top: 4px;
    margin-bottom: 8px;
  }}
  li {{
    margin-bottom: 2px;
  }}
  img {{
    max-width: 100%;
    max-height: 220px;
    object-fit: contain;
    border-radius: 6px;
    margin: 8px auto;
    display: block;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    break-inside: avoid;
    page-break-inside: avoid;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 11px;
    break-inside: avoid;
    page-break-inside: avoid;
  }}
  th, td {{
    border: 1px solid var(--border);
    padding: 5px 7px;
    text-align: left;
  }}
  th {{
    background-color: #f8fafc;
    font-weight: 600;
    color: #334155;
  }}
  tr:nth-child(even) {{
    background-color: #fdfdfd;
  }}
  blockquote {{
    border-left: 3px solid var(--accent);
    margin: 8px 0;
    padding: 6px 12px;
    background-color: #eff6ff;
    border-radius: 0 6px 6px 0;
    color: #1e40af;
    font-size: 11.5px;
    break-inside: avoid;
    page-break-inside: avoid;
  }}
  code {{
    background: #f1f5f9;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 0.9em;
    color: #b91c1c;
  }}
  hr {{
    border: none;
    border-top: 1px solid var(--border);
    margin: 16px 0;
  }}

  /* Mobile responsiveness on screen */
  @media screen and (max-width: 768px) {{
    .booklet-container {{
      column-count: 1;
      padding: 16px;
    }}
    .toolbar {{
      flex-direction: column;
      gap: 10px;
      text-align: center;
    }}
  }}

  /* Print optimization: 2-up on Landscape A4 with Center Fold Line */
  @media print {{
    @page {{
      size: A4 landscape;
      margin: 8mm 10mm;
    }}
    body {{
      background: white !important;
      color: #000 !important;
      font-size: 9pt !important;
      line-height: 1.38 !important;
      padding: 0 !important;
    }}
    .toolbar {{
      display: none !important;
    }}
    .booklet-container {{
      box-shadow: none !important;
      border-radius: 0 !important;
      padding: 0 !important;
      margin: 0 !important;
      max-width: 100% !important;
      width: 100% !important;
      column-count: 2 !important;
      column-gap: 16mm !important;
      column-rule: 1px dashed #94a3b8 !important; /* 對摺虛線 */
    }}
    h1 {{
      font-size: 13pt !important;
      margin-top: 4pt !important;
      margin-bottom: 4pt !important;
    }}
    h2 {{
      font-size: 11pt !important;
      margin-top: 10pt !important;
      margin-bottom: 4pt !important;
    }}
    h3, h4 {{
      font-size: 9.5pt !important;
      margin-top: 6pt !important;
      margin-bottom: 2pt !important;
    }}
    p, ul, ol {{
      margin-top: 2pt !important;
      margin-bottom: 4pt !important;
    }}
    table {{
      font-size: 7.5pt !important;
      margin: 4pt 0 !important;
    }}
    th, td {{
      padding: 3pt 4pt !important;
    }}
    blockquote {{
      padding: 3pt 6pt !important;
      margin: 3pt 0 !important;
      font-size: 8pt !important;
    }}
    img {{
      max-height: 150px !important;
      margin: 4pt auto !important;
    }}
  }}
</style>
</head>
<body>
<div class="toolbar">
  <div class="toolbar-title">
    <span>📖 A4 橫向雙頁小冊子版</span>
    <span class="toolbar-hint">(列印時每張 A4 紙包含左右兩頁，中間附對摺虛線，印出後直接對摺即成 A5 口袋手冊)</span>
  </div>
  <button class="print-btn" onclick="window.print()">🖨️ 列印小冊子 (Ctrl + P)</button>
</div>
<div class="booklet-container">
{body_html}
</div>
</body>
</html>
"""

    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"Generated Booklet HTML: {output_html_path}")

def generate_standard_html(md_file_path: str, output_html_path: str):
    """Generates a clean single-column responsive HTML for mobile/desktop reading."""
    md_path = Path(md_file_path).resolve()
    processed_md = get_processed_markdown(md_path)
    md = MarkdownIt('commonmark').enable('table')
    body_html = md.render(processed_md)
    title = md_path.stem.replace('_', ' ').title()

    html_template = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  :root {{
    --primary: #1e3a8a;
    --text: #1f2937;
    --bg: #f9fafb;
    --card-bg: #ffffff;
    --border: #e5e7eb;
    --accent: #2563eb;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Microsoft JhengHei", sans-serif;
    line-height: 1.7;
    color: var(--text);
    background-color: var(--bg);
    margin: 0;
    padding: 20px;
  }}
  .container {{
    max-width: 900px;
    margin: 0 auto;
    background: var(--card-bg);
    padding: 36px 48px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  }}
  h1 {{
    color: var(--primary);
    border-bottom: 2px solid var(--border);
    padding-bottom: 12px;
    margin-top: 0;
  }}
  h2 {{
    color: var(--primary);
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
    margin-top: 36px;
  }}
  h3, h4 {{
    color: #374151;
    margin-top: 24px;
  }}
  img {{
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    margin: 16px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 14px;
  }}
  th, td {{
    border: 1px solid var(--border);
    padding: 8px 12px;
    text-align: left;
  }}
  th {{
    background-color: #f3f4f6;
    font-weight: 600;
  }}
  tr:nth-child(even) {{
    background-color: #fafafa;
  }}
  blockquote {{
    border-left: 4px solid var(--accent);
    margin: 16px 0;
    padding: 10px 18px;
    background-color: #eff6ff;
    border-radius: 0 8px 8px 0;
    color: #1e40af;
  }}
  code {{
    background: #f3f4f6;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.9em;
    color: #b91c1c;
  }}
  hr {{
    border: none;
    border-top: 1px solid var(--border);
    margin: 32px 0;
  }}

  @media screen and (max-width: 600px) {{
    body {{
      padding: 10px;
    }}
    .container {{
      padding: 20px 16px;
      border-radius: 8px;
    }}
    table {{
      font-size: 13px;
      display: block;
      overflow-x: auto;
      white-space: nowrap;
    }}
  }}

  @media print {{
    body {{
      background: white;
      padding: 0;
    }}
    .container {{
      box-shadow: none;
      padding: 0;
      max-width: 100%;
    }}
    h1, h2, h3 {{
      page-break-after: avoid;
    }}
    table, img, blockquote {{
      page-break-inside: avoid;
    }}
  }}
</style>
</head>
<body>
<div class="container">
{body_html}
</div>
</body>
</html>
"""
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"Generated Standard HTML: {output_html_path}")

if __name__ == '__main__':
    base = Path(__file__).parent
    
    # 3 core documents requested by user
    core_files = [
        "trip_review_guide.md",
        "souvenir_guide.md",
        "trip_preparation_guide.md"
    ]
    
    for filename in core_files:
        src = base / filename
        if src.exists():
            stem = src.stem
            # 1. Standard HTML
            generate_standard_html(str(src), str(base / f"{stem}.html"))
            # 2. Booklet 2-up per A4 Landscape HTML
            generate_booklet_html(str(src), str(base / f"{stem}_booklet.html"))
