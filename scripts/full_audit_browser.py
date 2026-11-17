import asyncio
from playwright.async_api import async_playwright

async def full_audit():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(channel="chrome", headless=True)
        except Exception:
            browser = await p.chromium.launch(channel="msedge", headless=True)
            
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        errors = []
        page.on("console", lambda msg: errors.append(f"[{msg.type}] {msg.text}") if msg.type in ["error", "warning"] else None)
        page.on("pageerror", lambda err: errors.append(f"[pageerror] {err}"))
        
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(2500)
        
        # Test Three.js Studio canvas
        canvas = await page.query_selector("#studioInteractiveCanvas")
        print("Canvas found:", canvas is not None)
        
        # Test Tab clicks in WebGL section
        tabs = await page.query_selector_all(".studio-tab-btn")
        print("Studio tabs count:", len(tabs))
        for tab in tabs:
            await tab.click()
            await page.wait_for_timeout(500)
            
        # Test Before/After Slider drag
        slider = await page.query_selector(".comparison-slider-handle")
        if slider:
            box = await slider.bounding_box()
            if box:
                await page.mouse.move(box["x"] + box["width"]/2, box["y"] + box["height"]/2)
                await page.mouse.down()
                await page.mouse.move(box["x"] - 100, box["y"] + box["height"]/2)
                await page.mouse.up()
                print("Slider dragged successfully")
                
        # Test FAQ accordion
        faq_headers = await page.query_selector_all(".faq-accordion-header, .accordion-header, .faq-item")
        print("FAQ items count:", len(faq_headers))
        if faq_headers:
            await faq_headers[0].click()
            await page.wait_for_timeout(300)
            print("First FAQ item clicked")

        # Check for horizontal scroll / overflow
        scroll_width = await page.evaluate("() => document.documentElement.scrollWidth")
        client_width = await page.evaluate("() => document.documentElement.clientWidth")
        print(f"Viewport 1440px: scrollWidth={scroll_width}, clientWidth={client_width}")
        if scroll_width > client_width:
            print(f"WARNING: Horizontal overflow detected! diff = {scroll_width - client_width}px")
        else:
            print("SUCCESS: Zero horizontal overflow on 1440px desktop!")
            
        # Take comprehensive screenshot of index.html
        await page.screenshot(path="docs/screenshots/full_page_verified_audit.png", full_page=True)
        print("Captured full page verified audit screenshot")

        print("Console issues:", len(errors))
        for e in errors[:10]:
            print(" -", e)
            
        await browser.close()

asyncio.run(full_audit())
