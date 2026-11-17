import asyncio
from playwright.async_api import async_playwright

async def audit_all_button_hovers():
    print("=" * 60)
    print("AUDITING HOVER CONTRAST ON ALL BUTTONS")
    print("=" * 60)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel="chrome")
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        await page.wait_for_timeout(800)
        
        buttons = await page.query_selector_all("a.btn, button.btn, a.mobikasa-arrow-btn, a.btn-price-tier, a.btn-services-explore, a.btn-squad-action, .scanner-btn-submit, .btn-outline")
        print(f"Testing {len(buttons)} main interactive buttons...")
        
        issues = []
        for i, b in enumerate(buttons):
            text = (await b.text_content()).strip()[:30]
            await b.hover()
            await page.wait_for_timeout(100)
            
            style_data = await b.evaluate('''el => {
                const s = window.getComputedStyle(el);
                return {
                    color: s.color,
                    bg: s.backgroundColor,
                    tag: el.tagName,
                    cls: el.className
                };
            }''')
            
            # Simple check: if text color and bg color are too close (e.g. both white or both dark)
            color = style_data["color"]
            bg = style_data["bg"]
            
            # Check for white on white (rgb(255, 255, 255) on rgb(255, 245, 240) or similar)
            is_white_text = "255, 255, 255" in color or "255, 245" in color or "250, 250" in color
            is_white_bg = "255, 255, 255" in bg or "255, 245" in bg or "248, 250" in bg
            
            if is_white_text and is_white_bg:
                print(f"❌ [CRITICAL BUG] Button '{text}' (class: {style_data['cls']}): WHITE TEXT on WHITE BG! color={color}, bg={bg}")
                issues.append((text, style_data))
            else:
                print(f"   ✓ Button '{text}': color={color}, bg={bg}")
                
        print("\n" + "=" * 60)
        print(f"TOTAL HOVER BUGS FOUND: {len(issues)}")
        print("=" * 60)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(audit_all_button_hovers())
