import requests

urls = [
    ("docs/screenshots/transformation_redesign_dual.png", "01 - Dual View (Legacy vs 3D Headless).png", "https://mcp.figma.com/mcp/upload/0d6d4ba2-ac38-4f81-9cd0-f93554d60726/submit?scaleMode=FILL&currentPageId=0%3A1"),
    ("docs/screenshots/transformation_redesign_legacy.png", "02 - Legacy Monolith Tab.png", "https://mcp.figma.com/mcp/upload/7f3dbc64-c648-4a06-9735-d81bb4f147c3/submit?scaleMode=FILL&currentPageId=0%3A1"),
    ("docs/screenshots/transformation_redesign_modern.png", "03 - Modernized 3D Headless Tab.png", "https://mcp.figma.com/mcp/upload/04788a76-a670-4b08-886b-bb2bb65e6df4/submit?scaleMode=FILL&currentPageId=0%3A1")
]

for file_path, layer_name, submit_url in urls:
    print(f"Uploading {layer_name} to Figma canvas...")
    with open(file_path, "rb") as f:
        file_bytes = f.read()
    
    files = {"file": (layer_name, file_bytes, "image/png")}
    resp = requests.post(submit_url, files=files)
    print(f"Uploaded {layer_name}! Status:", resp.status_code, resp.text[:150])

print("All 3 frames placed on canvas successfully!")
