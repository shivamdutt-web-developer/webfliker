import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

targets = [
    'hero-section', 'kpi-section', 'services-section', 'methodology-section',
    'work-section', 'before-after-section', 'pricing-matrix-section',
    'comparison-section', 'testimonials-section', 'faq-section',
    'instant-scanner-section', 'cta-audit-section'
]

for t in targets:
    # search for .target { ... }
    m = re.search(r'\.' + t + r'\s*\{([^}]+)\}', css)
    if m:
        body = m.group(1)
        bg = [line.strip() for line in body.split(';') if 'background' in line]
        print(f".{t:<25} -> {bg}")
    else:
        print(f".{t:<25} -> (no direct rule)")
