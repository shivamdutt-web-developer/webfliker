import asyncio
from playwright.async_api import async_playwright

async def verify_clean_page():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(channel="chrome", headless=True)
        except Exception:
            browser = await p.chromium.launch(channel="msedge", headless=True)
            
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        errors = []
        page.on("console", lambda msg: errors.append(f"[{msg.type}] {msg.text}") if msg.type in ["error", "warning"] else None)
        page.on("pageerror", lambda err: errors.append(f"[pageerror] {err}"))
        
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        
        # Verify webgl-studio is completely gone
        studio = await page.query_selector("#webgl-studio")
        print("webgl-studio exists:", studio is not None)
        
        # Check horizontal overflow
        scroll_width = await page.evaluate("() => document.documentElement.scrollWidth")
        client_width = await page.evaluate("() => document.documentElement.clientWidth")
        print(f"Viewport 1440px: scrollWidth={scroll_width}, clientWidth={client_width}")
        
        print("Console errors count:", len(errors))
        for err in errors[:5]:
            print(" -", err)
            
        await page.screenshot(path="docs/screenshots/clean_page_no_webgl.png", full_page=False)
        print("Screenshot captured to docs/screenshots/clean_page_no_webgl.png")
        await browser.close()

asyncio.run(verify_clean_page())
