with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

s = text.find('id="transformation-showcase"')
e = text.find('</section>', s)
print(f"Section range: {s} to {e}, length={e-s}")
print(text[s:s+1200])
