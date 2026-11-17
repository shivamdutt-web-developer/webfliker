with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = "const cards = document.querySelectorAll('.service-card, .deliverable-box, .team-card, .price-card, .work-card, .portfolio-card');"
new_sel = "const cards = document.querySelectorAll('.service-card, .deliverable-box, .team-card, .price-card, .pricing-card, .work-card, .portfolio-card, .mobikasa-signature-card, .kpi-card, .process-step-card, .phase-item-card, .bento-card-square, .lighthouse-benchmark-card, .bento-perf-card, .testimonial-card, .review-card, .blog-card, .insight-card, .office-card, .global-office-card, .stitch-3d-card');"

if target in text:
    text = text.replace(target, new_sel)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated card tilt selector in app.js!")
else:
    print("WARNING: Target selector not found in app.js")
