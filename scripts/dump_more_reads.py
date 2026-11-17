import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 2850 <= i <= 2880:
            if 'read_file' in line or 'Showing lines' in line:
                data = json.loads(line)
                content = data.get('content', '')
                if 'Showing lines' in content:
                    lines_c = content.splitlines()
                    header = [l for l in lines_c[:5] if 'Showing lines' in l]
                    print(f"Line {i}: {header[0] if header else 'read'}")
                    with open(f'transcript_read_{i}.txt', 'w', encoding='utf-8') as out:
                        out.write(content)
