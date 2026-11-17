import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'index.html' in line and any(k in line for k in ['<section id="services"', '<section class="services-section"', '<section class="pricing-matrix-section"']):
            print(f"Line {i} has full section content! Line len={len(line)}")
            # Let's inspect what is in this line
            data = json.loads(line)
            # Find the tool call content or arguments
            tc = data.get('tool_calls', [])
            for c in tc:
                args = c.get('args', {})
                for k, v in args.items():
                    if isinstance(v, str) and 'services-section' in v:
                        print(f"   Found in tool_call arg '{k}': len={len(v)}")
                        with open(f'section_dump_{i}_{k}.txt', 'w', encoding='utf-8') as dump:
                            dump.write(v)
            content = data.get('content', '')
            if isinstance(content, str) and 'services-section' in content:
                print(f"   Found in content: len={len(content)}")
                with open(f'section_dump_{i}_content.txt', 'w', encoding='utf-8') as dump:
                    dump.write(content)
