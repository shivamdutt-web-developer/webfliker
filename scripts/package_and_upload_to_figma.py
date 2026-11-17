import os
import zipfile
import hashlib
import base64
import requests

archive_path = r"C:\tmp\figma-import-5fee2442c96a2d7dd1ef30915faaa68be18906f0dc224b8a93d171bd0d1c86a1.archive"
os.makedirs(os.path.dirname(archive_path), exist_ok=True)

# 1. Build ZIP archive of the project
exclude_dirs = {"node_modules", ".git", ".gemini", "docs", "scripts", "__pycache__", ".pytest_cache"}
exclude_exts = {".py", ".txt", ".docx", ".archive"}

print("Building archive at", archive_path)
file_count = 0
with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk("."):
        # filter dirs in place
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith(".")]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in exclude_exts:
                continue
            full_path = os.path.join(root, file)
            # relative path for archive root
            rel_path = os.path.relpath(full_path, ".").replace("\\", "/")
            zf.write(full_path, rel_path)
            file_count += 1

archive_size = os.path.getsize(archive_path)
print(f"Archive created! Files included: {file_count}, Size: {archive_size / 1024:.1f} KB")

# 2. Compute SHA256 checksum in base64
with open(archive_path, "rb") as f:
    archive_bytes = f.read()

sha256_digest = hashlib.sha256(archive_bytes).digest()
checksum_b64 = base64.b64encode(sha256_digest).decode("utf-8")
print("Computed SHA256 Base64 checksum:", checksum_b64)

# 3. Read exact upload fields from step output
import json
with open(r"C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\steps\4885\output.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

upload_info = data["upload"]
submit_url = upload_info["submitUrl"]
fields = dict(upload_info["fields"])

# S3 form fields
form_data = []
for k, v in fields.items():
    form_data.append((k, (None, v)))

form_data.append(("Content-Type", (None, "application/octet-stream")))
form_data.append(("x-amz-checksum-sha256", (None, checksum_b64)))
form_data.append(("file", ("archive.zip", archive_bytes, "application/octet-stream")))

print(f"Sending POST request to {submit_url}...")
resp = requests.post(submit_url, files=form_data)
print("Upload status code:", resp.status_code)
if resp.status_code in (200, 204):
    print("SUCCESS: Upload completed cleanly!")
else:
    print("Upload response body:", resp.text)
