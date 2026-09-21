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

def convert_md_to_standalone_html(md_file_path: str, output_html_path: str = None):
    md_path = Path(md_file_path).resolve()
    if not md_path.exists():
        print(f"File not found: {md_path}")
        return

    if output_html_path is None:
        output_html_path = md_path.with_suffix('.html')
    else:
        output_html_path = Path(output_html_path).resolve()

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Find local markdown images and replace with base64 data URI
    base_dir = md_path.parent

    def replace_img(match):
        alt = match.group(1)
        src = match.group(2)
        # Check if local file
        target_path = (base_dir / src).resolve()
        if target_path.exists() and target_path.is_file():
            data_uri = image_to_base64(target_path)
            return f'![{alt}]({data_uri})'
        return match.group(0)

    # Regex for ![alt](src)
    processed_md = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_img, md_text)

    # Initialize markdown-it with table support (avoiding linkify requirement)
    md = MarkdownIt('commonmark').enable('table')
    body_html = md.render(processed_md)

    # High-quality responsive & print-friendly template
    html_template = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{md_path.stem}</title>
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
    font-size: 15px;
  }}
  th, td {{
    border: 1px solid var(--border);
    padding: 10px 14px;
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

  /* Mobile optimization for iPhone */
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
    th, td {{
      padding: 8px 10px;
    }}
  }}

  /* Print optimization */
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

    print(f"Successfully generated standalone HTML: {output_html_path}")

if __name__ == '__main__':
    base = Path(__file__).parent
    # Convert souvenir_guide.md and trip_review_guide.md
    files_to_convert = [
        base / "souvenir_guide.md",
        base / "trip_review_guide.md"
    ]
    for md_file in files_to_convert:
        if md_file.exists():
            convert_md_to_standalone_html(str(md_file))
