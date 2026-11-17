import asyncio
from playwright.async_api import async_playwright

async def verify_turn():
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True, channel="chrome")
        page = await b.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(500)
        
        hero = await page.query_selector(".hero-section")
        box = await hero.bounding_box()
        scene = await page.query_selector("#hero3dScene")
        
        # Test 1: Move mouse far right
        await page.mouse.move(box["x"] + box["width"] * 0.9, box["y"] + box["height"] * 0.5)
        await page.wait_for_timeout(400)
        tf_right = await scene.evaluate("el => el.style.transform")
        print("Mouse at RIGHT edge -> Transform:", tf_right)
        
        # Capture screenshot turning right
        await page.screenshot(path="C:/Users/shiva/.gemini/antigravity/brain/2e7d2b96-cdc7-413f-bf71-e57580e857c8/model_turn_right.png")
        
        # Test 2: Move mouse far left
        await page.mouse.move(box["x"] + box["width"] * 0.1, box["y"] + box["height"] * 0.5)
        await page.wait_for_timeout(400)
        tf_left = await scene.evaluate("el => el.style.transform")
        print("Mouse at LEFT edge -> Transform:", tf_left)
        
        # Capture screenshot turning left
        await page.screenshot(path="C:/Users/shiva/.gemini/antigravity/brain/2e7d2b96-cdc7-413f-bf71-e57580e857c8/model_turn_left.png")
        
        # Test 3: Click and drag rotation
        stage = await page.query_selector("#hero3dStage")
        sbox = await stage.bounding_box()
        # Drag from center to left by 200px
        await page.mouse.move(sbox["x"] + sbox["width"] * 0.5, sbox["y"] + sbox["height"] * 0.5)
        await page.mouse.down()
        await page.mouse.move(sbox["x"] + sbox["width"] * 0.5 - 200, sbox["y"] + sbox["height"] * 0.5)
        await page.wait_for_timeout(200)
        tf_drag = await scene.evaluate("el => el.style.transform")
        print("While DRAGGING -> Transform:", tf_drag)
        await page.mouse.up()
        
        await b.close()

if __name__ == "__main__":
    asyncio.run(verify_turn())
