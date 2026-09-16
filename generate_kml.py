import csv

csv_path = r"c:\Code\Antigravity\Travel-Plan\google_maps_trip_import.csv"
kml_path = r"c:\Code\Antigravity\Travel-Plan\google_maps_trip_import.kml"

kml_header = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>歐洲自駕旅行地圖 (Travel-Plan)</name>
    <description>德奧捷 13 日純電自駕 — 核心停車場、住宿與站點標記</description>
"""

kml_footer = """  </Document>
</kml>
"""

placemarks = []

with open(csv_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        name = r["Name"]
        time_val = r["Time"]
        desc = r["Description"]
        addr = r["Address"]
        lat = r["Latitude"]
        lon = r["Longitude"]
        link = r["Google_Maps_Link"]
        
        desc_html = f"""<![CDATA[
          <p><b>類別：</b>{r['Category']}</p>
          <p><b>時間：</b>{time_val}</p>
          <p><b>地址：</b>{addr}</p>
          <p><b>說明：</b>{desc}</p>
          <p><a href="{link}" target="_blank">👉 在 Google Maps 中開啟導航</a></p>
        ]]>"""
        
        pm = f"""    <Placemark>
      <name>{name}</name>
      <description>{desc_html}</description>
      <Point>
        <coordinates>{lon},{lat},0</coordinates>
      </Point>
    </Placemark>"""
        placemarks.append(pm)

with open(kml_path, "w", encoding="utf-8") as f:
    f.write(kml_header + "\n".join(placemarks) + "\n" + kml_footer)

print("google_maps_trip_import.kml generated successfully!")
