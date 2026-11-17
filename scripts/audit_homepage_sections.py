import asyncio
import json
import os
from playwright.async_api import async_playwright

async def audit():
    os.makedirs('docs/screenshots/sections', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel='chrome')
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        
        errors = []
        page.on('console', lambda msg: errors.append(f'[{msg.type}] {msg.text}') if msg.type == 'error' else None)
        page.on('pageerror', lambda err: errors.append(f'[pageerror] {err}'))
        
        await page.goto('http://localhost:3000/index.html', wait_until='networkidle')
        await page.screenshot(path='docs/screenshots/full_homepage_current.png', full_page=True)
        
        sections = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('section, footer, .top-announcement-bar, .schbang-marquee-strip')).map((s, idx) => {
                const headingEl = s.querySelector('h1, h2, h3');
                return {
                    index: idx,
                    tagName: s.tagName.toLowerCase(),
                    id: s.id || '',
                    className: s.className || '',
                    heading: headingEl ? headingEl.innerText.replace(/\\n/g, ' ').trim() : '',
                    height: s.offsetHeight,
                    width: s.offsetWidth
                };
            });
        }''')
        
        print(f"Total sections detected: {len(sections)}")
        for s in sections:
            print(f"[{s['index']}] <{s['tagName']} id='{s['id']}' class='{s['className']}'> | Heading: {s['heading'][:50]} | H:{s['height']}px")
            
        print(f"\nConsole Errors: {len(errors)}")
        for err in errors:
            print(f"  - {err}")
            
        # Take individual screenshots of key sections to review design
        elements_to_capture = [
            '#hero',
            '.schbang-marquee-strip',
            '.accreditations-media-section',
            '#kpi',
            '#services',
            '#methodology',
            '#founder-spotlight',
            '#case-studies',
            '#transformation-showcase',
            '#pricing',
            '#comparison',
            '#milestones',
            '#testimonials',
            '#team-culture',
            '#blog',
            '#faq',
            '#instant-scanner',
            '#global-hubs',
            '#proposal',
            'footer'
        ]
        
        for sel in elements_to_capture:
            el = await page.query_selector(sel)
            if el:
                safe_name = sel.replace('#', '').replace('.', '').replace('-', '_')
                await el.screenshot(path=f'docs/screenshots/sections/{safe_name}.png')
                print(f"Captured {safe_name}.png")
                
        await browser.close()

if __name__ == '__main__':
    asyncio.run(audit())
