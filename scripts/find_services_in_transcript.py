import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

found = []
with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'services-section' in line:
            found.append(i)
            print(f"Match on line {i}, line len: {len(line)}")

print("Matches:", found)
