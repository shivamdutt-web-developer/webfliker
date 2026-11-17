import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'Showing lines' in line and 'of 2039' in line:
            data = json.loads(line)
            content = data.get('content', '')
            for l in content.splitlines()[:5]:
                if 'Showing lines' in l:
                    print(f"Line {i}: {l}")
                    with open(f"read_chunk_{i}.txt", "w", encoding="utf-8") as out:
                        out.write(content)
