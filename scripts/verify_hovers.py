import asyncio
from playwright.async_api import async_playwright

async def verify_hovers():
    print("=" * 60)
    print("VERIFYING BUTTON HOVERS AND FOUNDER SPOTLIGHT")
    print("=" * 60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel="chrome")
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000/index.html?v=1794805593", wait_until="networkidle")
        await page.wait_for_timeout(800)
        
        founder = await page.query_selector("#founder-spotlight")
        if founder:
            await founder.scroll_into_view_if_needed()
            await page.wait_for_timeout(400)
            
            # 1. Normal state
            await founder.screenshot(path="docs/screenshots/founder_spotlight_normal.png")
            print("Captured docs/screenshots/founder_spotlight_normal.png")
            
            # 2. Hover over Primary button
            btn_primary = await founder.query_selector(".founder-btn-primary")
            if btn_primary:
                await btn_primary.hover()
                await page.wait_for_timeout(300)
                await founder.screenshot(path="docs/screenshots/founder_btn_primary_hover.png")
                print("Captured docs/screenshots/founder_btn_primary_hover.png")
                
            # 3. Hover over Secondary button
            btn_sec = await founder.query_selector(".founder-btn-secondary")
            if btn_sec:
                await btn_sec.hover()
                await page.wait_for_timeout(300)
                await founder.screenshot(path="docs/screenshots/founder_btn_sec_hover.png")
                print("Captured docs/screenshots/founder_btn_sec_hover.png")
                
        # 4. Check Team Culture button hover
        team = await page.query_selector(".team-culture-section")
        if team:
            await team.scroll_into_view_if_needed()
            await page.wait_for_timeout(400)
            btn_life = await team.query_selector(".btn-outline-dark")
            if btn_life:
                await btn_life.hover()
                await page.wait_for_timeout(300)
                await team.screenshot(path="docs/screenshots/team_btn_hover.png")
                print("Captured docs/screenshots/team_btn_hover.png")
                
        await browser.close()
        print("Hover Verification Completed!")

if __name__ == "__main__":
    asyncio.run(verify_hovers())
