with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<a href="life-at-webflikr.html" class="btn btn-outline" style="border-color: #cbd5e1; color: #0f172a;">Life at Webflikr</a>',
    '<a href="life-at-webflikr.html" class="btn btn-outline-dark">Life at Webflikr</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

outline_dark_css = '''
.btn-outline-dark {
  background: transparent;
  border: 1.5px solid #cbd5e1;
  color: #0f172a !important;
  padding: 12px 24px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 0.92rem;
  text-decoration: none;
  transition: all 0.25s ease;
  display: inline-flex;
  align-items: center;
}
.btn-outline-dark:hover {
  border-color: #ff5e1e !important;
  color: #ff5e1e !important;
  background: #fff5f0 !important;
  transform: translateY(-2px);
}
'''

if '.btn-outline-dark' not in css:
    css += outline_dark_css
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)

print('Updated btn-outline-dark in index.html and styles.css!')
