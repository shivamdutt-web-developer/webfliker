import asyncio
from playwright.async_api import async_playwright

async def test_hero():
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True, channel="chrome")
        page = await b.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(600)
        
        # Resting capture
        await page.screenshot(path="C:/Users/shiva/.gemini/antigravity/brain/2e7d2b96-cdc7-413f-bf71-e57580e857c8/seamless_hero_resting.png")
        print("Captured seamless_hero_resting.png")
        
        # Hover over the phone to trigger 3D tilt
        stage = await page.query_selector("#hero3dStage")
        box = await stage.bounding_box()
        # Move mouse to top-right of stage
        await page.mouse.move(box["x"] + box["width"] * 0.75, box["y"] + box["height"] * 0.25)
        await page.wait_for_timeout(500)
        
        await page.screenshot(path="C:/Users/shiva/.gemini/antigravity/brain/2e7d2b96-cdc7-413f-bf71-e57580e857c8/seamless_hero_hover_tilt.png")
        print("Captured seamless_hero_hover_tilt.png")
        
        await b.close()

if __name__ == "__main__":
    asyncio.run(test_hero())
