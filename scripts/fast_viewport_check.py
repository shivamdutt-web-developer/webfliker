import asyncio
from playwright.async_api import async_playwright

VIEWPORTS = [
    ('320px', 320, 640),
    ('375px', 375, 667),
    ('390px', 390, 844),
    ('430px', 430, 932),
    ('768px', 768, 1024),
    ('1024px', 1024, 768),
    ('1280px', 1280, 800),
    ('1440px', 1440, 900),
    ('1920px', 1920, 1080)
]

async def check():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel='chrome')
        all_ok = True
        for name, w, h in VIEWPORTS:
            page = await browser.new_page(viewport={'width': w, 'height': h})
            await page.goto('http://localhost:3000/index.html', wait_until='domcontentloaded')
            await page.wait_for_timeout(300)
            res = await page.evaluate('''() => {
                const doc = document.documentElement.offsetWidth;
                const scroll = Math.max(document.documentElement.scrollWidth, document.body.scrollWidth);
                return { doc, scroll, ok: scroll <= doc + 1 };
            }''')
            if not res['ok']:
                all_ok = False
            print(f"Viewport {name}: doc={res['doc']}px, scroll={res['scroll']}px, PASS={res['ok']}")
            await page.close()
        await browser.close()
        print("ALL VIEWPORTS PASS:", all_ok)

if __name__ == '__main__':
    asyncio.run(check())
