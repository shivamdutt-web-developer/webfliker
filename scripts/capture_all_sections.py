import asyncio
import os
from playwright.async_api import async_playwright

async def capture_all():
    os.makedirs('docs/screenshots/sections', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel='chrome')
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        await page.goto('http://localhost:3000/index.html', wait_until='networkidle')
        
        sections = await page.query_selector_all('section, footer, .top-announcement-bar, .schbang-marquee-strip')
        for i, s in enumerate(sections):
            tag = await s.evaluate('el => el.tagName.toLowerCase()')
            s_id = await s.evaluate('el => el.id || ""')
            s_cls = await s.evaluate('el => (el.className || "").split(" ")[0]')
            name = s_id if s_id else s_cls
            filename = f"docs/screenshots/sections/{i:02d}_{name}.png"
            try:
                await s.screenshot(path=filename)
                print(f"Captured {filename}")
            except Exception as e:
                print(f"Failed {filename}: {e}")
                
        await browser.close()

if __name__ == '__main__':
    asyncio.run(capture_all())
