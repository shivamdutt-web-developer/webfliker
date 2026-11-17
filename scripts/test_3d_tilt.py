import asyncio
from playwright.async_api import async_playwright

async def test_3d_mouse_interactions():
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
        
        stage = page.locator("#hero3dStage")
        print("Stage found:", await stage.count())
        
        # Take resting state screenshot
        await stage.screenshot(path="docs/screenshots/3d_stage_resting.png")
        print("Captured 3d_stage_resting.png")
        
        # Get bounding box of stage
        box = await stage.bounding_box()
        print("Stage bounding box:", box)
        
        # 1. Move mouse to right-top of stage
        await page.mouse.move(box["x"] + box["width"] * 0.85, box["y"] + box["height"] * 0.25)
        await page.wait_for_timeout(600)
        
        # Check transforms
        scene_transform = await page.evaluate("() => document.getElementById('hero3dScene').style.transform")
        card_transform = await page.evaluate("() => document.getElementById('layerSalesCard').style.transform")
        print("Scene transform on mouse move:", scene_transform)
        print("Sales Card transform on mouse move:", card_transform)
        
        # Capture tilted hover state
        await stage.screenshot(path="docs/screenshots/3d_stage_tilted_hover.png")
        print("Captured 3d_stage_tilted_hover.png")
        
        # 2. Move mouse away to trigger mouseleave
        await page.mouse.move(10, 10)
        await page.wait_for_timeout(1000)
        
        reset_transform = await page.evaluate("() => document.getElementById('hero3dScene').style.transform")
        print("Scene transform after mouseleave:", reset_transform)
        
        # Check for horizontal overflow
        scroll_width = await page.evaluate("() => document.documentElement.scrollWidth")
        client_width = await page.evaluate("() => document.documentElement.clientWidth")
        print(f"Viewport 1440px: scrollWidth={scroll_width}, clientWidth={client_width}")
        
        print("Console errors count:", len(errors))
        for err in errors[:5]:
            print(" -", err)
            
        await browser.close()

asyncio.run(test_3d_mouse_interactions())
