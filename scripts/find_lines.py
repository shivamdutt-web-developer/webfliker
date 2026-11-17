with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'hero-section' in line or 'schbang-marquee' in line or 'webgl-lab-section' in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
