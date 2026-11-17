import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'apply_seamless_mobikasa_phone.py' in line:
            print(f"Step on line {i}")
