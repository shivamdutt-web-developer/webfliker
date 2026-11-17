# 1. Revert styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

marker = "/* ==========================================================================\n   GOOGLE STITCH DESIGN SYSTEM & 3D INTERACTION OVERHAUL"
idx = css.find(marker)
if idx != -1:
    reverted_css = css[:idx].rstrip() + "\n"
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(reverted_css)
    print("SUCCESS: Removed Stitch CSS from styles.css!")
else:
    print("Marker not found in styles.css!")

# 2. Revert app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = "const cards = document.querySelectorAll('.service-card, .deliverable-box, .team-card, .price-card, .pricing-card, .work-card, .portfolio-card, .mobikasa-signature-card, .kpi-card, .process-step-card, .phase-item-card, .bento-card-square, .lighthouse-benchmark-card, .bento-perf-card, .testimonial-card, .review-card, .blog-card, .insight-card, .office-card, .global-office-card, .stitch-3d-card');"
orig = "const cards = document.querySelectorAll('.service-card, .deliverable-box, .team-card, .price-card, .work-card, .portfolio-card');"

if target in js:
    js = js.replace(target, orig)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("SUCCESS: Reverted init3dCardTilt selector in app.js!")
else:
    print("Target selector not found in app.js")

print("COMPLETE REVERT DONE!")
