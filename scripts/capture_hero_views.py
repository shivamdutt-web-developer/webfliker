import os
from playwright.sync_api import sync_playwright

ws_dir = os.path.abspath("docs/screenshots")
os.makedirs(ws_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    
    console_errors = []
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    
    print("Opening page...")
    page.goto("http://localhost:3000/index.html", wait_until="networkidle")
    page.wait_for_timeout(1500)
    
    hero = page.locator("#hero")
    
    # View 1: 3D Search Lens (Default)
    print("Capturing View 1: 3D Search Lens...")
    hero.screenshot(path=os.path.join(ws_dir, "hero_3d_view_1_search_lens.png"))
    
    # View 2: 3D AI Entity Graph
    print("Clicking 3D AI Entity Graph...")
    page.click("#btnHeroNeural")
    page.wait_for_timeout(1000)
    hero.screenshot(path=os.path.join(ws_dir, "hero_3d_view_2_neural_graph.png"))
    
    # View 3: 3D Storefront
    print("Clicking 3D Storefront...")
    page.click("#btnHeroPhone")
    page.wait_for_timeout(800)
    hero.screenshot(path=os.path.join(ws_dir, "hero_3d_view_3_storefront.png"))
    
    browser.close()
    
    print("Console errors count:", len(console_errors), console_errors)
    print("All 3 Hero states captured successfully!")
