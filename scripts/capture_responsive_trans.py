from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    
    # Tablet (768px)
    page_tablet = browser.new_page(viewport={'width': 768, 'height': 1024})
    page_tablet.goto('http://localhost:3000/index.html', wait_until='networkidle')
    page_tablet.wait_for_timeout(800)
    sec_tablet = page_tablet.locator('#transformation-showcase')
    sec_tablet.scroll_into_view_if_needed()
    page_tablet.wait_for_timeout(400)
    sec_tablet.screenshot(path='docs/screenshots/trans_tablet_768.png')
    
    # Mobile (390px)
    page_mobile = browser.new_page(viewport={'width': 390, 'height': 844})
    page_mobile.goto('http://localhost:3000/index.html', wait_until='networkidle')
    page_mobile.wait_for_timeout(800)
    sec_mobile = page_mobile.locator('#transformation-showcase')
    sec_mobile.scroll_into_view_if_needed()
    page_mobile.wait_for_timeout(400)
    sec_mobile.screenshot(path='docs/screenshots/trans_mobile_390.png')
    
    browser.close()
    print("Captured tablet and mobile views successfully!")
