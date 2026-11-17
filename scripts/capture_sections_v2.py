import asyncio
from playwright.async_api import async_playwright
import os

async def capture():
    os.makedirs('docs/screenshots', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel='chrome')
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        await page.goto('http://localhost:3000/index.html', wait_until='domcontentloaded')
        await page.wait_for_timeout(1000)

        # 1. Founder Spotlight
        el = page.locator('#founder-spotlight')
        if await el.count() > 0:
            await el.screenshot(path='docs/screenshots/founder_spotlight_v2.png')
            print('Captured docs/screenshots/founder_spotlight_v2.png')

        # 2. Case Studies & SERP Table
        el = page.locator('.rankings-proof-card')
        if await el.count() > 0:
            await el.screenshot(path='docs/screenshots/serp_proof_table_v2.png')
            print('Captured docs/screenshots/serp_proof_table_v2.png')

        # 3. Transformation Showcase
        el = page.locator('#transformation-showcase')
        if await el.count() > 0:
            await el.screenshot(path='docs/screenshots/transformation_v2.png')
            print('Captured docs/screenshots/transformation_v2.png')

        # 4. Instant Scanner
        el = page.locator('#instant-scanner')
        if await el.count() > 0:
            await el.screenshot(path='docs/screenshots/instant_scanner_v2.png')
            print('Captured docs/screenshots/instant_scanner_v2.png')

        # 5. Full page scroll view around founder spotlight
        await page.screenshot(path='docs/screenshots/founder_context_v2.png', clip={'x': 0, 'y': 2800, 'width': 1440, 'height': 1000})
        print('Captured docs/screenshots/founder_context_v2.png')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(capture())
