import asyncio
from playwright.async_api import async_playwright

async def inspect_mobikasa_canvas():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("https://www.mobikasa.com/", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        
        info = await page.evaluate('''() => {
            const canvas = document.querySelector('canvas');
            const h1 = document.querySelector('h1');
            const hero = h1 ? h1.closest('section') || h1.parentElement.parentElement : null;
            return {
                canvasDetails: canvas ? {
                    width: canvas.width,
                    height: canvas.height,
                    className: canvas.className,
                    id: canvas.id,
                    parentHTML: canvas.parentElement ? canvas.parentElement.outerHTML.slice(0, 1000) : ''
                } : null,
                heroText: hero ? hero.innerText : '',
                heroHTML: hero ? hero.outerHTML.slice(0, 2000) : ''
            };
        }''')
        
        print("Canvas details:", info["canvasDetails"])
        print("\nHero Text:\n", info["heroText"][:500])
        print("\nHero HTML snippet:\n", info["heroHTML"][:800])
        await browser.close()

asyncio.run(inspect_mobikasa_canvas())
