with open('styles.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'search-command-stage' in l or 'search-terminal-card' in l or 'hero-visual-col' in l:
        print(f"Line {i+1}: {l.strip()[:100]}")
