with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<h3 class="trans-card-title text-legacy-title">', '<h3 class="trans-card-title text-legacy-title" style="color: #ffffff !important;">')
html = html.replace('<h3 class="trans-card-title text-modern-title">', '<h3 class="trans-card-title text-modern-title" style="color: #ffffff !important;">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write('''
body.theme-light .transformation-showcase-section h1,
body.theme-light .transformation-showcase-section h2,
body.theme-light .transformation-showcase-section h3,
body.theme-light .transformation-showcase-section h4,
body.theme-light .transformation-showcase-section .trans-card-title,
.transformation-showcase-section h1,
.transformation-showcase-section h2,
.transformation-showcase-section h3,
.transformation-showcase-section h4,
.transformation-showcase-section .trans-card-title {
  color: #ffffff !important;
}
''')

print("Applied strict white color overrides to transformation H3s")
