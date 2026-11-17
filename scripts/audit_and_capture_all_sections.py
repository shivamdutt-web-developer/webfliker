import asyncio
import os
from playwright.async_api import async_playwright

async def capture_all():
    os.makedirs('docs/screenshots/audit_sections', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel='chrome')
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        await page.goto('http://localhost:3000/index.html', wait_until='networkidle')
        await page.wait_for_timeout(800)
        
        sections = await page.evaluate('''() => {
            const list = [];
            document.querySelectorAll('section, footer').forEach((s, idx) => {
                const heading = s.querySelector('h1, h2, h3');
                list.push({
                    index: idx,
                    id: s.id || '',
                    cls: s.className || '',
                    heading: heading ? heading.innerText.trim().slice(0, 40) : '',
                    tag: s.tagName.toLowerCase()
                });
            });
            return list;
        }''')
        
        print(f"Found {len(sections)} sections/footer to audit.")
        
        for s in sections:
            # query selector
            selector = f"{s['tag']}"
            if s['id']:
                selector += f"#{s['id']}"
            elif s['cls']:
                # take first class
                first_cls = s['cls'].split()[0]
                selector += f".{first_cls}"
            
            # Select the nth matching element
            elements = await page.query_selector_all(s['tag'])
            for el_idx, el in enumerate(elements):
                el_id = await el.evaluate('e => e.id')
                el_cls = await el.evaluate('e => e.className')
                if el_id == s['id'] and (not s['cls'] or s['cls'].split()[0] in el_cls):
                    await el.scroll_into_view_if_needed()
                    await page.wait_for_timeout(300)
                    safe_name = f"{s['index']:02d}_{s['id'] or s['cls'].split()[0]}"
                    path = f"docs/screenshots/audit_sections/{safe_name}.png"
                    await el.screenshot(path=path)
                    print(f"Captured [{s['index']}] {safe_name} -> {path}")
                    break
                    
        await browser.close()

if __name__ == '__main__':
    asyncio.run(capture_all())
