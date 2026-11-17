import asyncio
from playwright.async_api import async_playwright

async def validate_polished_hero():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(channel="chrome", headless=True)
        except Exception:
            browser = await p.chromium.launch(channel="msedge", headless=True)
            
        # 1. Desktop Test (1440x900)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        errors = []
        page.on("console", lambda msg: errors.append(f"[{msg.type}] {msg.text}") if msg.type in ["error", "warning"] else None)
        page.on("pageerror", lambda err: errors.append(f"[pageerror] {err}"))
        
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        
        # Test Lucide icons
        await page.evaluate("() => { if (window.lucide) lucide.createIcons(); }")
        await page.wait_for_timeout(500)
        
        # Capture Desktop Full Hero Screenshot
        hero = page.locator("#hero")
        await hero.screenshot(path="docs/screenshots/polished_hero_desktop.png")
        print("Captured docs/screenshots/polished_hero_desktop.png")
        
        # Test Mouse Hover Interaction
        stage = page.locator("#hero3dStage")
        await stage.hover(position={"x": 380, "y": 140})
        await page.wait_for_timeout(400)
        
        hover_data = await page.evaluate('''() => {
            const scene = document.getElementById('hero3dScene');
            const revCard = document.getElementById('layerRevenueCard');
            const rankBadge = document.getElementById('layerRankBadge');
            const aiCard = document.getElementById('layerAiCard');
            return {
                sceneTransform: scene.style.transform,
                revTransform: revCard ? revCard.style.transform : '',
                rankTransform: rankBadge ? rankBadge.style.transform : '',
                aiTransform: aiCard ? aiCard.style.transform : ''
            };
        }''')
        print("Hover Data:", hover_data)
        await stage.screenshot(path="docs/screenshots/polished_hero_hover_tilt.png")
        print("Captured docs/screenshots/polished_hero_hover_tilt.png")
        
        # Test Mouse Leave
        await page.mouse.move(10, 10)
        await page.wait_for_timeout(600)
        leave_data = await page.evaluate('''() => document.getElementById('hero3dScene').style.transform''')
        print("Reset transform after leave:", leave_data)
        
        # Check Desktop Horizontal Overflow
        sw = await page.evaluate("() => document.documentElement.scrollWidth")
        cw = await page.evaluate("() => document.documentElement.clientWidth")
        print(f"Desktop 1440px: scrollWidth={sw}, clientWidth={cw}")
        
        # 2. Mobile Test (390x844 - iPhone 14)
        mobile_page = await browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
        await mobile_page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await mobile_page.wait_for_timeout(2000)
        
        mobile_hero = mobile_page.locator("#hero")
        await mobile_hero.screenshot(path="docs/screenshots/polished_hero_mobile.png")
        print("Captured docs/screenshots/polished_hero_mobile.png")
        
        msw = await mobile_page.evaluate("() => document.documentElement.scrollWidth")
        mcw = await mobile_page.evaluate("() => document.documentElement.clientWidth")
        print(f"Mobile 390px: scrollWidth={msw}, clientWidth={mcw}")
        
        print("Console errors count:", len(errors))
        for e in errors[:5]:
            print(" -", e)
            
        await browser.close()

asyncio.run(validate_polished_hero())
