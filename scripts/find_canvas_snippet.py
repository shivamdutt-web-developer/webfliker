with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'studioInteractiveCanvas' in l:
        start = max(0, i - 10)
        end = min(len(lines), i + 100)
        print("".join(lines[start:end]))
        break
