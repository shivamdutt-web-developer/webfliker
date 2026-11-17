p = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

terms = ['Danetti Luxury Living', 'Navneet Kaushal', 'Dentalkart.com', 'Bronze Plan', '4-Stage Search Authority']

with open(p, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        for t in terms:
            if t in line:
                print(f"Line {i} matched term '{t}' (len={len(line)})")
                break
