import os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    
    console_errors = []
    page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)
    
    page.goto('http://localhost:3000/index.html', wait_until='networkidle')
    page.wait_for_timeout(1000)
    
    section = page.locator('#transformation-showcase')
    section.scroll_into_view_if_needed()
    page.wait_for_timeout(600)
    
    os.makedirs('docs/screenshots', exist_ok=True)
    art_dir = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8'
    
    # 1. Dual View
    path_dual_ws = 'docs/screenshots/transformation_redesign_dual.png'
    path_dual_art = os.path.join(art_dir, 'transformation_redesign_dual.png')
    section.screenshot(path=path_dual_ws)
    section.screenshot(path=path_dual_art)
    
    # 2. Legacy Tab
    page.click('#btnViewLegacy')
    page.wait_for_timeout(500)
    path_legacy_ws = 'docs/screenshots/transformation_redesign_legacy.png'
    path_legacy_art = os.path.join(art_dir, 'transformation_redesign_legacy.png')
    section.screenshot(path=path_legacy_ws)
    section.screenshot(path=path_legacy_art)
    
    # 3. Modern Tab
    page.click('#btnViewModern')
    page.wait_for_timeout(500)
    path_modern_ws = 'docs/screenshots/transformation_redesign_modern.png'
    path_modern_art = os.path.join(art_dir, 'transformation_redesign_modern.png')
    section.screenshot(path=path_modern_ws)
    section.screenshot(path=path_modern_art)
    
    # Return to Dual View
    page.click('#btnViewSplit')
    page.wait_for_timeout(500)
    
    browser.close()
    
    print('Console errors:', len(console_errors), console_errors)
    print('Successfully captured all 3 tabs!')
