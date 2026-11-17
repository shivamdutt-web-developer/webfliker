import asyncio
from playwright.async_api import async_playwright

async def inspect_point():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="chrome", headless=True)
        page = await b.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        
        info = await page.evaluate('''() => {
            const stage = document.getElementById('hero3dStage');
            const box = stage.getBoundingClientRect();
            const x = box.left + 250;
            const y = box.top + 250;
            const els = document.elementsFromPoint(x, y);
            return {
                box,
                x, y,
                els: els.map(e => ({
                    tag: e.tagName,
                    id: e.id,
                    cls: e.className,
                    pointerEvents: window.getComputedStyle(e).pointerEvents,
                    zIndex: window.getComputedStyle(e).zIndex,
                    position: window.getComputedStyle(e).position
                }))
            };
        }''')
        
        print("Box:", info["box"])
        print("Point:", info["x"], info["y"])
        for e in info["els"]:
            print(" -", e)
        await b.close()

asyncio.run(inspect_point())
