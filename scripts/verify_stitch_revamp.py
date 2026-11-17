import os
from playwright.sync_api import sync_playwright

ws_dir = os.path.abspath("docs/screenshots")
os.makedirs(ws_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    
    console_errors = []
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    
    page.goto("http://localhost:3000/index.html", wait_until="networkidle")
    page.wait_for_timeout(1000)
    
    # 1. Check Hero Section with Stitch
    hero = page.locator("#hero")
    hero.screenshot(path=os.path.join(ws_dir, "stitch_revamp_01_hero.png"))
    
    # 2. Check Services / Growth Modules
    services = page.locator("#services")
    services.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    services.screenshot(path=os.path.join(ws_dir, "stitch_revamp_02_services.png"))
    
    # 3. Check Methodology
    method = page.locator("#methodology")
    method.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    method.screenshot(path=os.path.join(ws_dir, "stitch_revamp_03_methodology.png"))
    
    # 4. Check Pricing
    pricing = page.locator("#pricing")
    pricing.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    pricing.screenshot(path=os.path.join(ws_dir, "stitch_revamp_04_pricing.png"))
    
    # 5. Check Scanner & CTA
    scanner = page.locator("#instant-scanner")
    scanner.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    scanner.screenshot(path=os.path.join(ws_dir, "stitch_revamp_05_scanner.png"))
    
    # 6. Overflow check
    scroll_w = page.evaluate("document.documentElement.scrollWidth")
    client_w = page.evaluate("document.documentElement.clientWidth")
    overflow = scroll_w - client_w
    
    browser.close()
    
    print("Console errors count:", len(console_errors), console_errors)
    print("Desktop overflow:", overflow)
    print("All Stitch revamp screenshots captured successfully!")
