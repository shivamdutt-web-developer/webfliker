with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = -1
end = -1
for i, l in enumerate(lines):
    if 'id="webgl-studio"' in l or 'class="webgl-lab-section"' in l:
        start = i
    if start != -1 and '</section>' in l and i > start:
        end = i
        break

print(f"webgl-studio section found from line {start+1} to {end+1}")
print("".join(lines[start:start+10]))
print("...")
print("".join(lines[end-5:end+1]))
