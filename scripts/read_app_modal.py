with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'initProposalModal' in l:
        print(f"Line {i+1}: {l}")
        start = max(0, i-5)
        end = min(len(lines), i+15)
        print("".join(lines[start:end]))
