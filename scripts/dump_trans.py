with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = 66168
end = 76767
with open('scripts/current_trans.html', 'w', encoding='utf-8') as f:
    f.write(html[start:end])
print("Saved scripts/current_trans.html")
