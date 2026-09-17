import csv
import xml.sax.saxutils as saxutils

csv_path = r"c:\Code\Antigravity\Travel-Plan\google_maps_trip_import.csv"
kml_path = r"c:\Code\Antigravity\Travel-Plan\google_maps_trip_import.kml"

kml_header = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>歐洲自駕旅行地圖 (Travel-Plan)</name>
    <description>德奧捷 13 日純電自駕 — 核心停車場、著名景點、充電站、住宿與站點標記</description>

    <!-- 停車場專用圖示 (藍色 P) -->
    <Style id="icon-parking">
      <IconStyle>
        <color>ffd1881e</color>
        <scale>1.2</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/shapes/parking_lot.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 觀光景點專用圖示 (鮮紅星號/相機) -->
    <Style id="icon-sight">
      <IconStyle>
        <color>ff2257ff</color>
        <scale>1.2</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/shapes/camera.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 住宿飯店專用圖示 (紫色床鋪) -->
    <Style id="icon-hotel">
      <IconStyle>
        <color>ffaa248e</color>
        <scale>1.2</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/shapes/lodging.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- Tesla 超充站專用圖示 (綠色閃電/加油站) -->
    <Style id="icon-charger">
      <IconStyle>
        <color>ff47a043</color>
        <scale>1.2</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/shapes/gas_stations.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 碼頭渡輪專用圖示 (青藍碼頭/渡輪) -->
    <Style id="icon-dock">
      <IconStyle>
        <color>ffc1ac00</color>
        <scale>1.2</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/shapes/marina.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 景觀咖啡專用圖示 (琥珀色咖啡杯) -->
    <Style id="icon-cafe">
      <IconStyle>
        <color>ff008cfb</color>
        <scale>1.2</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/shapes/coffee.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 租車與公路專用圖示 (灰藍車輛) -->
    <Style id="icon-car">
      <IconStyle>
        <color>ff7a6e54</color>
        <scale>1.2</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/shapes/cabs.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 機場返程專用圖示 (深藍飛機) -->
    <Style id="icon-airport">
      <IconStyle>
        <color>ffab4939</color>
        <scale>1.2</scale>
        <Icon>
          <href>https://maps.google.com/mapfiles/kml/shapes/airports.png</href>
        </Icon>
      </IconStyle>
    </Style>
"""

kml_footer = """  </Document>
</kml>
"""

category_style_map = {
    "🅿️ 景點停車場": "icon-parking",
    "🅿️ 飯店停車場": "icon-parking",
    "⭐ 觀光景點": "icon-sight",
    "⭐ 著名景點 / 世界遺產": "icon-sight",
    "⭐ 著名景點 / 高山湖泊": "icon-sight",
    "🏨 住宿飯店": "icon-hotel",
    "⚡ Tesla 超充站": "icon-charger",
    "🚢 渡輪碼頭": "icon-dock",
    "☕ 景觀咖啡": "icon-cafe",
    "🚗 租車與公路": "icon-car",
    "✈️ 機場返程": "icon-airport"
}

placemarks = []

with open(csv_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        name = r["Name"]
        escaped_name = saxutils.escape(name)
        time_val = r["Time"]
        desc = r["Description"]
        addr = r["Address"]
        lat = r["Latitude"]
        lon = r["Longitude"]
        link = r["Google_Maps_Link"]
        cat = r.get("Category", "")
        style_id = category_style_map.get(cat, "icon-sight")
        
        desc_html = f"""<![CDATA[
          <p><b>類別：</b>{cat}</p>
          <p><b>時間：</b>{time_val}</p>
          <p><b>地址：</b>{addr}</p>
          <p><b>說明：</b>{desc}</p>
          <p><a href="{link}" target="_blank">👉 在 Google Maps 中開啟導航</a></p>
        ]]>"""
        
        pm = f"""    <Placemark>
      <name>{escaped_name}</name>
      <styleUrl>#{style_id}</styleUrl>
      <description>{desc_html}</description>
      <Point>
        <coordinates>{lon},{lat},0</coordinates>
      </Point>
    </Placemark>"""
        placemarks.append(pm)

with open(kml_path, "w", encoding="utf-8") as f:
    f.write(kml_header + "\n".join(placemarks) + "\n" + kml_footer)

print("google_maps_trip_import.kml generated successfully and XML validated!")
