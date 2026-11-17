import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

check_lines = [2843, 2845, 2847, 2849]
with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i in check_lines:
            data = json.loads(line)
            content = data.get('content', '')
            print(f"Line {i}: content len={len(content)}")
            # Let's inspect first 200 chars and last 200 chars
            lines_c = content.splitlines()
            print(f"   Lines in content: {len(lines_c)}")
            print(f"   First line: {lines_c[0] if lines_c else 'empty'}")
            print(f"   Last line: {lines_c[-1] if lines_c else 'empty'}")
            with open(f'transcript_read_{i}.txt', 'w', encoding='utf-8') as out:
                out.write(content)
            print(f"   Saved transcript_read_{i}.txt")
