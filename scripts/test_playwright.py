import asyncio
from playwright.async_api import async_playwright

async def capture_sections():
    async with async_playwright() as p:
        # Launch using installed Google Chrome or Microsoft Edge
        try:
            browser = await p.chromium.launch(channel="chrome", headless=True)
            print("Launched Chrome")
        except Exception:
            browser = await p.chromium.launch(channel="msedge", headless=True)
            print("Launched Edge")
            
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        
        # Take hero section
        hero = page.locator("#hero")
        if await hero.count() > 0:
            await hero.screenshot(path="docs/screenshots/current_hero.png")
            print("Captured hero section")
            
        # Take webgl studio section
        studio = page.locator("#webgl-studio")
        if await studio.count() > 0:
            await studio.screenshot(path="docs/screenshots/current_webgl_studio.png")
            print("Captured webgl studio section")

        print("Console errors count:", len(errors))
        if errors:
            print("Console Errors:", errors[:5])
            
        await browser.close()

asyncio.run(capture_sections())
