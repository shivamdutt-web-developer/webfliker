import asyncio
from playwright.async_api import async_playwright

VIEWPORTS = [
    {"name": "Mobile Mini (320px)", "width": 320, "height": 640},
    {"name": "iPhone 14 Pro Max (430px)", "width": 430, "height": 932},
    {"name": "Tablet Portrait (768px)", "width": 768, "height": 1024},
    {"name": "Desktop HD (1280px)", "width": 1280, "height": 800},
    {"name": "MacBook / Desktop 2K (1440px)", "width": 1440, "height": 900},
    {"name": "Large Desktop Full HD (1920px)", "width": 1920, "height": 1080}
]

async def verify_and_capture():
    print("=" * 60)
    print("RUNNING COMPLETE VISUAL AUDIT & QA VERIFICATION")
    print("=" * 60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel="chrome")
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        errors = []
        page.on("console", lambda msg: errors.append(f"[{msg.type}] {msg.text}") if msg.type == "error" else None)
        page.on("pageerror", lambda err: errors.append(f"[pageerror] {err}"))
        
        await page.goto("http://localhost:3000/index.html?v=1794804351", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        print(f"\n1. Console Error Audit: {len(errors)} errors found")
        for err in errors:
            print(f"   ERROR: {err}")
            
        # Capture updated sections
        sections = [
            ("services", "mobikasa_services_bento.png"),
            ("transformation-showcase", "mobikasa_trans_stage.png"),
            ("pricing", "mobikasa_pricing_3tier.png"),
            ("instant-scanner", "mobikasa_scanner_clean.png")
        ]
        
        print("\n2. Capturing Section Screenshots:")
        for sec_id, filename in sections:
            el = await page.query_selector(f"#{sec_id}")
            if el:
                await el.screenshot(path=f"docs/screenshots/{filename}")
                print(f"   ✅ Captured docs/screenshots/{filename}")
            else:
                print(f"   ❌ Could not find #{sec_id}")
                
        # Test billing toggle click in pricing
        print("\n3. Testing Pricing Interactive Toggle:")
        toggle_btn = await page.query_selector("#pricingToggleBtn")
        if toggle_btn:
            # Click quarterly
            await toggle_btn.click()
            await page.wait_for_timeout(300)
            q_price = await page.evaluate("() => document.querySelector('.price-amount').textContent")
            print(f"   Quarterly price displayed after toggle click: ₹{q_price}")
            await toggle_btn.click()
            await page.wait_for_timeout(300)
            m_price = await page.evaluate("() => document.querySelector('.price-amount').textContent")
            print(f"   Monthly price displayed after 2nd toggle click: ₹{m_price}")
            
        # Test 9 viewports for horizontal overflow
        print("\n4. Testing Horizontal Overflow across viewports:")
        for vp in VIEWPORTS:
            v_page = await browser.new_page(viewport={"width": vp["width"], "height": vp["height"]})
            await v_page.goto("http://localhost:3000/index.html?v=1794804351", wait_until="networkidle")
            
            overflow = await v_page.evaluate('''() => {
                const docWidth = document.documentElement.offsetWidth;
                const scrollWidth = document.documentElement.scrollWidth;
                const bodyScroll = document.body.scrollWidth;
                const maxScroll = Math.max(scrollWidth, bodyScroll);
                return { docWidth, maxScroll, hasOverflow: maxScroll > docWidth + 1 };
            }''')
            
            if overflow["hasOverflow"]:
                print(f"   ❌ {vp['name']} OVERFLOW: doc={overflow['docWidth']}px, scroll={overflow['maxScroll']}px")
            else:
                print(f"   ✅ {vp['name']}: Passed (doc={overflow['docWidth']}px, scroll={overflow['maxScroll']}px)")
            await v_page.close()
            
        await browser.close()
        print("\nVerification Complete!")

if __name__ == "__main__":
    asyncio.run(verify_and_capture())
