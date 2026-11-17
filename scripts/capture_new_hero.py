import asyncio
from playwright.async_api import async_playwright

async def capture_new_hero():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(channel="chrome", headless=True)
        except Exception:
            browser = await p.chromium.launch(channel="msedge", headless=True)
            
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        
        hero = page.locator("#hero")
        await hero.screenshot(path="docs/screenshots/updated_hero_mobikasa.png")
        print("Captured updated hero screenshot to docs/screenshots/updated_hero_mobikasa.png")
        
        await browser.close()

asyncio.run(capture_new_hero())
