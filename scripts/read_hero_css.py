with open('styles.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '.hero-section' in l:
        print(f"Line {i+1}: {l}")
        print("".join(lines[i:i+35]))
