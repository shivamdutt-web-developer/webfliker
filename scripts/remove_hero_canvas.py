# Remove hero3dCanvas from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<canvas id="hero3dCanvas" class="hero-3d-canvas"></canvas>\n          '
if target in html:
    html = html.replace(target, '')
else:
    target2 = '<canvas id="hero3dCanvas" class="hero-3d-canvas"></canvas>'
    html = html.replace(target2, '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: hero3dCanvas completely removed from index.html!")
