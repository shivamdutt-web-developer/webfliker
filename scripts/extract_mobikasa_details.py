import asyncio
from playwright.async_api import async_playwright

async def get_mobikasa_dom():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("https://www.mobikasa.com/", wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)
        
        info = await page.evaluate('''() => {
            const h1 = document.querySelector('h1');
            const parent = h1 ? h1.parentElement.parentElement : document.body;
            return {
                title: document.title,
                h1: h1 ? h1.innerText : '',
                heroClasses: parent ? parent.className : '',
                html: parent ? parent.innerHTML.slice(0, 4000) : ''
            };
        }''')
        
        print("Title:", info["title"])
        print("H1:", info["h1"])
        print("Hero Classes:", info["heroClasses"])
        print("HTML snippet:\n", info["html"][:1500])
        await browser.close()

asyncio.run(get_mobikasa_dom())
