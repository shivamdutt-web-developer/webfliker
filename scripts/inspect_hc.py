import asyncio
from playwright.async_api import async_playwright

async def inspect_hero_container():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="chrome", headless=True)
        page = await b.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        
        info = await page.evaluate('''() => {
            const hc = document.querySelector('.hero-container');
            const hvc = document.querySelector('.hero-visual-col');
            const stage = document.getElementById('hero3dStage');
            return {
                hc: hc ? {
                    rect: hc.getBoundingClientRect(),
                    pointerEvents: window.getComputedStyle(hc).pointerEvents,
                    overflow: window.getComputedStyle(hc).overflow,
                    zIndex: window.getComputedStyle(hc).zIndex
                } : null,
                hvc: hvc ? {
                    rect: hvc.getBoundingClientRect(),
                    pointerEvents: window.getComputedStyle(hvc).pointerEvents,
                    overflow: window.getComputedStyle(hvc).overflow,
                    zIndex: window.getComputedStyle(hvc).zIndex
                } : null,
                stage: stage ? {
                    rect: stage.getBoundingClientRect(),
                    pointerEvents: window.getComputedStyle(stage).pointerEvents,
                    overflow: window.getComputedStyle(stage).overflow,
                    zIndex: window.getComputedStyle(stage).zIndex
                } : null
            };
        }''')
        print(info)
        await b.close()

asyncio.run(inspect_hero_container())
