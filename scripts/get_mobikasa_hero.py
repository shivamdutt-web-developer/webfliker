import asyncio
from playwright.async_api import async_playwright

async def inspect_mobikasa():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("https://www.mobikasa.com/", wait_until="domcontentloaded")
        await page.wait_for_timeout(2000)
        
        # Get hero elements
        hero_html = await page.evaluate('''() => {
            const h1 = document.querySelector('h1');
            const heroSection = h1 ? h1.closest('section') || h1.parentElement.parentElement : document.querySelector('section');
            return {
                heading: h1 ? h1.innerText : '',
                html: heroSection ? heroSection.outerHTML.slice(0, 3000) : '',
                hasVideo: !!heroSection.querySelector('video'),
                hasCanvas: !!heroSection.querySelector('canvas'),
                videoSrc: heroSection.querySelector('video') ? heroSection.querySelector('video').src : '',
                imgs: Array.from(heroSection.querySelectorAll('img')).map(i => ({ src: i.src, alt: i.alt, className: i.className }))
            };
        }''')
        
        print("Hero heading:", hero_html["heading"])
        print("Has Video:", hero_html["hasVideo"])
        print("Video Src:", hero_html["videoSrc"])
        print("Has Canvas:", hero_html["hasCanvas"])
        print("Images count:", len(hero_html["imgs"]))
        for img in hero_html["imgs"][:5]:
            print(" - Img:", img)
            
        await page.screenshot(path="docs/screenshots/mobikasa_hero_direct.png")
        print("Screenshot saved to docs/screenshots/mobikasa_hero_direct.png")
        await browser.close()

asyncio.run(inspect_mobikasa())
