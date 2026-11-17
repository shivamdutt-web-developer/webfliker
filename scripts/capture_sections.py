import asyncio
from playwright.async_api import async_playwright

async def capture_sections():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        # Listen for console errors
        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        
        # Take full page screenshot
        await page.screenshot(path="docs/screenshots/current_index_desktop.png", full_page=True)
        print("Captured full page desktop screenshot")
        
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
            
        # Take work / case studies section
        work = page.locator("#case-studies")
        if await work.count() > 0:
            await work.screenshot(path="docs/screenshots/current_case_studies.png")
            print("Captured case studies section")

        # Take before-after transformation
        ba = page.locator("#transformation-showcase")
        if await ba.count() > 0:
            await ba.screenshot(path="docs/screenshots/current_transformation.png")
            print("Captured transformation showcase")
            
        print("Console errors count:", len(errors))
        if errors:
            print("Errors:", errors[:5])
            
        await browser.close()

asyncio.run(capture_sections())
