import os
import time
from playwright.sync_api import sync_playwright

art_dir = r"C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8"
ws_dir = os.path.abspath("docs/screenshots")
os.makedirs(ws_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    context = browser.new_context(
        viewport={"width": 1440, "height": 900},
        device_scale_factor=1.5
    )
    page = context.new_page()
    
    print("Navigating to http://localhost:3000/index.html...")
    page.goto("http://localhost:3000/index.html", wait_until="networkidle")
    page.wait_for_timeout(1500)
    
    # Smooth scroll down to trigger all animations, charts, dynamic elements, and lazy loads
    total_height = page.evaluate("document.body.scrollHeight")
    current = 0
    step = 700
    while current < total_height:
        current += step
        page.evaluate(f"window.scrollTo(0, {current})")
        page.wait_for_timeout(150)
    
    # Wait for any delayed animations at the bottom
    page.wait_for_timeout(1000)
    
    # Scroll back to top smoothly
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(1000)
    
    # Full Page Capture
    full_ws = os.path.join(ws_dir, "homepage_full_layout.png")
    full_art = os.path.join(art_dir, "homepage_full_layout.png")
    
    print("Capturing full page layout...")
    page.screenshot(path=full_ws, full_page=True)
    page.screenshot(path=full_art, full_page=True)
    
    # Check dimensions and size
    file_size_mb = os.path.getsize(full_ws) / (1024 * 1024)
    print(f"Full page screenshot saved! Size: {file_size_mb:.2f} MB")
    
    # Also capture segmented high-res parts in case Stitch needs modular sections
    sections = [
        ("01_hero_and_marquee", "#hero, .hero-section, header"),
        ("02_transformation_showcase", "#transformation-showcase"),
        ("03_serp_dominance_table", "#serp-dominance, .serp-dominance-section"),
        ("04_growth_modules", "#services, .growth-modules-section, #architecture"),
        ("05_founder_commitment", ".founder-commitment-section, #founder")
    ]
    
    for s_name, s_selector in sections:
        try:
            loc = page.locator(s_selector).first
            if loc.count() > 0:
                loc.scroll_into_view_if_needed()
                page.wait_for_timeout(400)
                s_path_ws = os.path.join(ws_dir, f"section_{s_name}.png")
                s_path_art = os.path.join(art_dir, f"section_{s_name}.png")
                loc.screenshot(path=s_path_ws)
                loc.screenshot(path=s_path_art)
                print(f"Captured section: {s_name}")
        except Exception as e:
            print(f"Section {s_name} skipped: {e}")
            
    browser.close()
    print("Done!")
