import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if len(line) > 50000 and ('<section class="services-section"' in line or 'id="services"' in line):
            print(f"Line {i}: Length {len(line)}")
            # Try to extract
            try:
                data = json.loads(line)
                def find_html(obj):
                    if isinstance(obj, str) and '<!DOCTYPE html>' in obj and '</html>' in obj:
                        return obj
                    elif isinstance(obj, dict):
                        for v in obj.values():
                            res = find_html(v)
                            if res: return res
                    elif isinstance(obj, list):
                        for item in obj:
                            res = find_html(item)
                            if res: return res
                    return None
                
                h = find_html(data)
                if h:
                    l = len(h.splitlines())
                    print(f"   Extracted HTML with {l} lines!")
                    if l > 1500:
                        with open('index_full_restored.html', 'w', encoding='utf-8') as out:
                            out.write(h)
                        print(f"   SAVED to index_full_restored.html from line {i}!")
            except Exception as e:
                print(f"   JSON parse error on line {i}: {e}")
