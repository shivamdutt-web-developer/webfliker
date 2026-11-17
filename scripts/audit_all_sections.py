import os
from playwright.sync_api import sync_playwright

ws_dir = os.path.abspath("docs/screenshots/audit")
os.makedirs(ws_dir, exist_ok=True)

sections_to_audit = [
    ("01_hero", "#hero"),
    ("03_kpi", ".kpi-section"),
    ("04_services", "#services"),
    ("05_methodology", "#methodology"),
    ("06_founder", "#founder-spotlight"),
    ("07_work", "#case-studies"),
    ("08_transformation", "#transformation-showcase"),
    ("09_pricing", "#pricing"),
    ("10_comparison", "#comparison"),
    ("11_milestones", "#milestones"),
    ("12_testimonials", ".testimonials-section"),
    ("15_faq", "#faq"),
    ("16_scanner", "#instant-scanner"),
    ("18_proposal", "#proposal")
]

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto("http://localhost:3000/index.html", wait_until="domcontentloaded")
    page.wait_for_timeout(1000)
    
    for name, selector in sections_to_audit:
        try:
            loc = page.locator(selector).first
            if loc.count() > 0:
                loc.scroll_into_view_if_needed()
                page.wait_for_timeout(300)
                path = os.path.join(ws_dir, f"{name}.png")
                loc.screenshot(path=path)
                print(f"Captured: {name}")
            else:
                print(f"Not found: {selector}")
        except Exception as e:
            print(f"Error capturing {name}: {e}")
            
    browser.close()
    print("Audit capture complete!")
