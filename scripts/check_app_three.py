with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
canvas_code = re.findall(r'studioInteractiveCanvas[\s\S]*?(?=function|var |let |const |$)', code)
if canvas_code:
    print("Found canvas code in app.js, length:", len(canvas_code[0]))
    print(canvas_code[0][:600])
else:
    print("Not found directly by that regex, searching for Three.js initialization")
    three_matches = re.findall(r'THREE\.[\s\S]{1,200}', code)
    print("THREE references count:", len(three_matches))
    for m in three_matches[:5]:
        print(" -", m.replace('\n', ' ')[:100])
