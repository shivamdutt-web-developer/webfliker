import asyncio
from playwright.async_api import async_playwright

async def capture_highlights():
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True, channel="chrome")
        page = await b.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        sections = [
            ("hero_showcase", ".hero-section"),
            ("trust_strip", ".accreditations-media-section"),
            ("kpi_grid", ".kpi-section"),
            ("services_bento", "#services"),
            ("founder_spotlight", ".founder-spotlight-section"),
            ("serp_radar_showcase", "#case-studies"),
            ("pricing_packages", "#pricing")
        ]
        
        for name, sel in sections:
            el = await page.query_selector(sel)
            if el:
                await el.scroll_into_view_if_needed()
                await page.wait_for_timeout(400)
                path = f"C:/Users/shiva/.gemini/antigravity/brain/2e7d2b96-cdc7-413f-bf71-e57580e857c8/elevated_{name}.png"
                await el.screenshot(path=path)
                print(f"Captured: {name} -> {path}")
                
        await b.close()

if __name__ == "__main__":
    asyncio.run(capture_highlights())
