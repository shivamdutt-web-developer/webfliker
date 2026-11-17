with open('styles.css', 'a', encoding='utf-8') as f:
    f.write('''
/* High-Contrast Visibility Overrides for Obsidian Dark Containers */
body.theme-light .rankings-proof-card h1,
body.theme-light .rankings-proof-card h2,
body.theme-light .rankings-proof-card h3,
body.theme-light .rankings-proof-card h4,
body.theme-light .rankings-proof-card .rankings-table-title,
.rankings-proof-card h1,
.rankings-proof-card h2,
.rankings-proof-card h3,
.rankings-proof-card h4,
.rankings-proof-card .rankings-table-title {
  color: #ffffff !important;
}

body.theme-light .rankings-proof-card p,
.rankings-proof-card p {
  color: #94a3b8 !important;
}

body.theme-light .founder-spotlight-section h1,
body.theme-light .founder-spotlight-section h2,
body.theme-light .founder-spotlight-section h3,
body.theme-light .founder-spotlight-section h4,
.founder-spotlight-section h1,
.founder-spotlight-section h2,
.founder-spotlight-section h3,
.founder-spotlight-section h4 {
  color: #ffffff !important;
}
''')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<h3 class="rankings-table-title">', '<h3 class="rankings-table-title" style="color: #ffffff !important;">')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated styles and html')
