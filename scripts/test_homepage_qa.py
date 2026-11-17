import asyncio
from playwright.async_api import async_playwright

VIEWPORTS = [
    {"name": "Mobile Mini (320px)", "width": 320, "height": 640},
    {"name": "iPhone SE (375px)", "width": 375, "height": 667},
    {"name": "iPhone 12/13/14 (390px)", "width": 390, "height": 844},
    {"name": "iPhone 14 Pro Max (430px)", "width": 430, "height": 932},
    {"name": "Tablet Portrait (768px)", "width": 768, "height": 1024},
    {"name": "Tablet Landscape (1024px)", "width": 1024, "height": 768},
    {"name": "Desktop HD (1280px)", "width": 1280, "height": 800},
    {"name": "MacBook / Desktop 2K (1440px)", "width": 1440, "height": 900},
    {"name": "Large Desktop Full HD (1920px)", "width": 1920, "height": 1080}
]

async def run_qa():
    print("=" * 60)
    print("STARTING COMPLETE HOMEPAGE QA & RESPONSIVENESS AUDIT")
    print("=" * 60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel="chrome")
        
        # Test 1: Desktop QA & 3D Tilt Testing
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        errors = []
        page.on("console", lambda msg: errors.append(f"[{msg.type}] {msg.text}") if msg.type == "error" else None)
        page.on("pageerror", lambda err: errors.append(f"[pageerror] {err}"))
        
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        print(f"\n1. Console Error Audit: {len(errors)} errors found")
        for err in errors:
            print(f"   ERROR: {err}")
            
        # Test 2: Interactive 3D Card Hover & Tilt Verification
        print("\n2. Testing 3D Tilt Card Interaction:")
        bento_card = await page.query_selector(".bento-card")
        if bento_card:
            box = await bento_card.bounding_box()
            # Hover over top-left of the card
            await page.mouse.move(box["x"] + box["width"] * 0.25, box["y"] + box["height"] * 0.25)
            await page.wait_for_timeout(300)
            
            transform = await bento_card.evaluate("el => el.style.transform")
            sheen_x = await bento_card.evaluate("el => el.style.getPropertyValue('--sheen-x')")
            sheen_y = await bento_card.evaluate("el => el.style.getPropertyValue('--sheen-y')")
            print(f"   Hover state transform: {transform}")
            print(f"   Specular Sheen coordinates: X={sheen_x}, Y={sheen_y}")
            
            # Hover leave
            await page.mouse.move(10, 10)
            await page.wait_for_timeout(300)
            reset_transform = await bento_card.evaluate("el => el.style.transform")
            print(f"   Mouse leave reset transform: {reset_transform}")
            
        # Test 3: Responsive Overflow Audit across all 9 viewports
        print("\n3. Testing Horizontal Overflow across 9 viewports:")
        all_passed = True
        for vp in VIEWPORTS:
            v_page = await browser.new_page(viewport={"width": vp["width"], "height": vp["height"]})
            await v_page.goto("http://localhost:3000/index.html", wait_until="networkidle")
            
            overflow_data = await v_page.evaluate('''() => {
                const docWidth = document.documentElement.offsetWidth;
                const scrollWidth = document.documentElement.scrollWidth;
                const bodyScroll = document.body.scrollWidth;
                const maxScroll = Math.max(scrollWidth, bodyScroll);
                const hasOverflow = maxScroll > docWidth + 1; // 1px tolerance
                
                let offending = [];
                if (hasOverflow) {
                    document.querySelectorAll('*').forEach(el => {
                        const r = el.getBoundingClientRect();
                        if (r.right > docWidth + 1) {
                            offending.push({
                                tag: el.tagName,
                                id: el.id,
                                cls: el.className,
                                right: r.right,
                                docWidth: docWidth
                            });
                        }
                    });
                }
                return { docWidth, maxScroll, hasOverflow, offending: offending.slice(0, 5) };
            }''')
            
            if overflow_data["hasOverflow"]:
                all_passed = False
                print(f"   ❌ {vp['name']} OVERFLOW: width={overflow_data['docWidth']}, scroll={overflow_data['maxScroll']}")
                for off in overflow_data["offending"]:
                    print(f"      Offender: <{off['tag']} id='{off['id']}' class='{off['cls']}'> right={off['right']}")
            else:
                print(f"   ✅ {vp['name']}: Passed (doc={overflow_data['docWidth']}px, scroll={overflow_data['maxScroll']}px)")
            await v_page.close()
            
        print("\n" + "=" * 60)
        print(f"OVERALL QA AUDIT: {'ALL TESTS PASSED WITH 0 BUGS' if (len(errors) == 0 and all_passed) else 'ATTENTION NEEDED'}")
        print("=" * 60)
        
        # Take full page screenshot of the elevated homepage
        await page.screenshot(path="docs/screenshots/elevated_homepage_final.png", full_page=True)
        print("Captured docs/screenshots/elevated_homepage_final.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_qa())
