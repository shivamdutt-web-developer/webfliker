with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Navneet Kaushal' in line or 'Last Search Agency' in line:
        start = max(0, i - 15)
        end = min(len(lines), i + 40)
        print("".join(lines[start:end]))
        break
