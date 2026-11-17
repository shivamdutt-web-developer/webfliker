import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'
found_steps = []
with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'index.html' in line and ('html lang="en"' in line or '<!DOCTYPE html>' in line):
            print(f"Found HTML dump on line {i}")
            found_steps.append((i, len(line)))

print(f"Total found: {len(found_steps)}")
if found_steps:
    last_line_idx = found_steps[-1][0]
    print(f"Inspecting last line: {last_line_idx}")
