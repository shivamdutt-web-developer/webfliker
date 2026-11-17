import requests

urls = [
    ("docs/screenshots/homepage_full_layout_web.jpg", "00 - Full Homepage Layout (Header to Footer).jpg", "image/jpeg", "https://mcp.figma.com/mcp/upload/dd8ae650-1fc0-4e08-abe2-8cdace3b6473/submit?scaleMode=FILL&currentPageId=0%3A1"),
    ("docs/screenshots/part_1_of_5.png", "04 - Hero Section & Enterprise Marquee.png", "image/png", "https://mcp.figma.com/mcp/upload/f9dac92c-d046-4b59-a776-6e310de69c33/submit?scaleMode=FILL&currentPageId=0%3A1"),
    ("docs/screenshots/part_3_of_5.png", "05 - SERP Dominance & Growth Architecture.png", "image/png", "https://mcp.figma.com/mcp/upload/8ede1127-6cc5-4af6-9a96-8850b18e4b43/submit?scaleMode=FILL&currentPageId=0%3A1"),
    ("docs/screenshots/part_4_of_5.png", "06 - Founder Commitment & Case Studies.png", "image/png", "https://mcp.figma.com/mcp/upload/eccc0dcc-4bf7-4c77-94d3-4663c48ef9ff/submit?scaleMode=FILL&currentPageId=0%3A1"),
    ("docs/screenshots/part_5_of_5.png", "07 - Comparison Matrix, FAQ & Global Footer.png", "image/png", "https://mcp.figma.com/mcp/upload/a6547e72-99b0-4c1e-86de-11e395a266ce/submit?scaleMode=FILL&currentPageId=0%3A1")
]

for file_path, layer_name, mime_type, submit_url in urls:
    print(f"Uploading {layer_name}...")
    with open(file_path, "rb") as f:
        file_bytes = f.read()
    
    files = {"file": (layer_name, file_bytes, mime_type)}
    resp = requests.post(submit_url, files=files)
    print(f"Uploaded {layer_name}! Status:", resp.status_code, resp.text[:120])

print("All section frames placed on Figma canvas!")
