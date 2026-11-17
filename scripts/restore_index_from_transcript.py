import json
import re

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

target_lines = [3511, 2263, 1914, 1502, 1498]
with open(transcript_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx in target_lines:
            # Search for <!DOCTYPE html> ... </html>
            start_m = line.find('<!DOCTYPE html>')
            if start_m != -1:
                end_m = line.find('</html>', start_m)
                if end_m != -1:
                    raw_html = line[start_m:end_m + len('</html>')]
                    # Unescape json string escapes like \n, \", etc.
                    # Since it was in JSON, json.loads of the line is safer:
                    try:
                        data = json.loads(line)
                        content_str = json.dumps(data)
                        # Find within data
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
                        
                        html_extracted = find_html(data)
                        if html_extracted:
                            line_count = len(html_extracted.splitlines())
                            print(f"Line {idx}: Successfully extracted HTML with {line_count} lines")
                            if line_count > 1500:
                                with open(f'index_backup_line_{idx}.html', 'w', encoding='utf-8') as out:
                                    out.write(html_extracted)
                                print(f"Saved index_backup_line_{idx}.html")
                    except Exception as e:
                        print(f"Error on line {idx}: {e}")
