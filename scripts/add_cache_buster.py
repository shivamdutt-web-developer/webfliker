import time

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

ts = str(int(time.time()))
text = text.replace('href="styles.css"', f'href="styles.css?v={ts}"')
text = text.replace('src="app.js"', f'src="app.js?v={ts}"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Added cache buster v={ts}")
