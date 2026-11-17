import asyncio
from playwright.async_api import async_playwright

async def audit_all_headings():
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True, channel="chrome")
        page = await b.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000/index.html", wait_until="networkidle")
        
        results = await page.evaluate('''() => {
            const list = [];
            document.querySelectorAll('h1, h2, h3, h4').forEach(h => {
                const style = window.getComputedStyle(h);
                let parent = h.parentElement;
                let bg = 'transparent';
                while (parent && (bg === 'transparent' || bg === 'rgba(0, 0, 0, 0)')) {
                    bg = window.getComputedStyle(parent).backgroundColor;
                    parent = parent.parentElement;
                }
                list.push({
                    tag: h.tagName,
                    text: h.innerText.slice(0, 45).replace(/\\n/g, ' '),
                    color: style.color,
                    bg: bg,
                    cls: h.className
                });
            });
            return list;
        }''')
        
        print(f"Total headings audited: {len(results)}")
        bad_contrast = []
        for h in results:
            print(f"<{h['tag']}> '{h['text']}' -> color={h['color']}, bg={h['bg']}")
            # Check if dark text on dark bg
            # rgb(15, 23, 42) is dark
            if "rgb(15, 23, 42)" in h['color'] and any(d in h['bg'] for d in ["rgb(7, 11, 20)", "rgb(11, 15, 25)", "rgb(9, 11, 16)", "rgb(17, 24, 39)", "rgb(8, 11, 18)"]):
                bad_contrast.append(h)
                
        print("\n" + "="*50)
        print(f"CRITICAL CONTRAST BUGS FOUND: {len(bad_contrast)}")
        for b_item in bad_contrast:
            print(f"   BUG: <{b_item['tag']}> '{b_item['text']}' color={b_item['color']} on bg={b_item['bg']}")
            
        await b.close()

if __name__ == "__main__":
    asyncio.run(audit_all_headings())
