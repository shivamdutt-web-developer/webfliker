import asyncio
from playwright.async_api import async_playwright

async def test_hover():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="chrome", headless=True)
        page = await b.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        stage = page.locator("#hero3dStage")
        
        # Hover with Playwright
        await stage.hover(position={"x": 400, "y": 100})
        await page.wait_for_timeout(300)
        
        # Read inline and computed style
        res = await page.evaluate('''() => {
            const scene = document.getElementById('hero3dScene');
            const card = document.getElementById('layerSalesCard');
            const sheen = document.getElementById('phoneLightSheen');
            return {
                sceneInline: scene.style.transform,
                sceneComputed: window.getComputedStyle(scene).transform,
                cardInline: card.style.transform,
                sheenX: sheen.style.getPropertyValue('--sheen-x'),
                sheenY: sheen.style.getPropertyValue('--sheen-y')
            };
        }''')
        print("Hover test results:", res)
        
        # Capture tilted hover state
        await stage.screenshot(path="docs/screenshots/3d_stage_active_hover.png")
        print("Screenshot saved to docs/screenshots/3d_stage_active_hover.png")
        
        await b.close()

asyncio.run(test_hover())
