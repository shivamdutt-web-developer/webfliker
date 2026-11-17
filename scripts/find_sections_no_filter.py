import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if '<section class="services-section"' in line or 'class="pricing-matrix-section"' in line:
            print(f"Line {i}: len={len(line)}")
            data = json.loads(line)
            # Find in tool_calls
            for tc in data.get('tool_calls', []):
                for k, v in tc.get('args', {}).items():
                    if isinstance(v, str) and ('pricing-matrix-section' in v or 'services-section' in v):
                        print(f"   Line {i} tc arg {k}: len={len(v)}")
                        with open(f'dump_{i}_{k}.txt', 'w', encoding='utf-8') as out:
                            out.write(v)
            content = data.get('content', '')
            if isinstance(content, str) and ('pricing-matrix-section' in content or 'services-section' in content):
                print(f"   Line {i} content: len={len(content)}")
                with open(f'dump_{i}_content.txt', 'w', encoding='utf-8') as out:
                    out.write(content)
