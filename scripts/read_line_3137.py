import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 3137:
            data = json.loads(line)
            print(f"Step {data.get('step_index')}, type: {data.get('type')}")
            for k in data.keys():
                print(f"Key {k}: {type(data[k])}")
            content = data.get('content', '')
            print("Content preview:", content[:500])
            break
