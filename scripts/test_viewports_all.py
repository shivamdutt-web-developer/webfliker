import asyncio
from playwright.async_api import async_playwright

VIEWPORTS = [320, 375, 390, 430, 768, 1024, 1280, 1440, 1920]

async def test_viewports():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(channel="chrome", headless=True)
        except Exception:
            browser = await p.chromium.launch(channel="msedge", headless=True)
            
        all_passed = True
        for w in VIEWPORTS:
            page = await browser.new_page(viewport={"width": w, "height": 800})
            await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
            await page.wait_for_timeout(1000)
            
            scroll_width = await page.evaluate("() => document.documentElement.scrollWidth")
            client_width = await page.evaluate("() => document.documentElement.clientWidth")
            
            if scroll_width > client_width:
                diff = scroll_width - client_width
                print(f"[FAIL] Viewport {w}px: overflow by {diff}px (scrollWidth={scroll_width}, clientWidth={client_width})")
                all_passed = False
            else:
                print(f"[PASS] Viewport {w}px: OK (scrollWidth={scroll_width}, clientWidth={client_width})")
                
            await page.close()
            
        await browser.close()
        if all_passed:
            print("\nALL 9 VIEWPORTS PASSED WITH ZERO HORIZONTAL OVERFLOW!")

asyncio.run(test_viewports())
