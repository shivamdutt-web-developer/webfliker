with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

in_flag = '<span class="hub-flag-badge flag-in">🇮🇳</span>'
gb_flag = '<span class="hub-flag-badge flag-gb">🇬🇧</span>'
us_flag = '<span class="hub-flag-badge flag-us">🇺🇸</span>'

# Or stylish stylized SVG pill flags
in_svg = '''<span class="hub-flag-circle">
  <svg viewBox="0 0 36 36" width="32" height="32" style="border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.12);">
    <path fill="#FF9933" d="M36 18c0-9.9-8.1-18-18-18S0 8.1 0 18s8.1 18 18 18 18-8.1 18-18z"/>
    <path fill="#FFFFFF" d="M0 12h36v12H0z"/>
    <path fill="#128807" d="M0 24h36c-2.3 7-8.8 12-16.5 12C11.8 36 5.3 31 3 24z"/>
    <circle fill="#000080" cx="18" cy="18" r="3.5"/>
  </svg>
</span>'''

gb_svg = '''<span class="hub-flag-circle">
  <svg viewBox="0 0 36 36" width="32" height="32" style="border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.12);">
    <path fill="#00247D" d="M36 18c0-9.9-8.1-18-18-18S0 8.1 0 18s8.1 18 18 18 18-8.1 18-18z"/>
    <path fill="#FFF" d="M36 15H21V0h-6v15H0v6h15v15h6V21h15z"/>
    <path fill="#CF142B" d="M36 16.5H20.5V0h-5v16.5H0v3h15.5V36h5V19.5H36z"/>
  </svg>
</span>'''

us_svg = '''<span class="hub-flag-circle">
  <svg viewBox="0 0 36 36" width="32" height="32" style="border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.12);">
    <path fill="#B22234" d="M36 18c0-9.9-8.1-18-18-18S0 8.1 0 18s8.1 18 18 18 18-8.1 18-18z"/>
    <path fill="#FFF" d="M0 10h36v3H0zm0 6h36v3H0zm0 6h36v3H0z"/>
    <path fill="#3C3B6E" d="M0 18c0-9.9 8.1-18 18-18v18H0z"/>
    <circle fill="#FFF" cx="9" cy="9" r="2.5"/>
  </svg>
</span>'''

# Replace in Hub 1 (Delhi)
html = html.replace('<span class="hub-flag">🇮🇳</span>', in_svg, 1)
# Replace in Hub 2 (Mumbai)
html = html.replace('<span class="hub-flag">🇮🇳</span>', in_svg, 1)
# Replace in Hub 3 (London)
html = html.replace('<span class="hub-flag">🇬🇧</span>', gb_svg, 1)
# Replace in Hub 4 (Chicago)
html = html.replace('<span class="hub-flag">🇺🇸</span>', us_svg, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated flags to SVG successfully!')
