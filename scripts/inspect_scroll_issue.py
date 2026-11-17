import asyncio
from playwright.async_api import async_playwright

async def inspect_scroll():
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True, channel='chrome')
        page = await b.new_page(viewport={'width': 1440, 'height': 900})
        await page.goto('http://localhost:3000/index.html', wait_until='networkidle')
        
        info = await page.evaluate('''() => {
            const body = document.body;
            const html = document.documentElement;
            const sections = Array.from(document.querySelectorAll('section')).map(s => ({
                id: s.id,
                cls: s.className,
                display: window.getComputedStyle(s).display,
                visibility: window.getComputedStyle(s).visibility,
                height: s.offsetHeight,
                top: s.getBoundingClientRect().top
            }));
            
            return {
                bodyScrollHeight: body.scrollHeight,
                docScrollHeight: html.scrollHeight,
                bodyOverflow: window.getComputedStyle(body).overflow,
                bodyOverflowY: window.getComputedStyle(body).overflowY,
                htmlOverflow: window.getComputedStyle(html).overflow,
                htmlOverflowY: window.getComputedStyle(html).overflowY,
                sectionCount: sections.length,
                sections: sections
            };
        }''')
        
        print('Scroll Info: bodyScrollHeight=', info['bodyScrollHeight'], 'docScrollHeight=', info['docScrollHeight'])
        print('Overflow Body:', info['bodyOverflow'], info['bodyOverflowY'])
        print('Overflow HTML:', info['htmlOverflow'], info['htmlOverflowY'])
        print('Total sections found:', info['sectionCount'])
        for s in info['sections']:
            print(f"Section #{s['id']} ({s['cls']}) -> display={s['display']}, height={s['height']}px, top={s['top']}")
            
        await b.close()

if __name__ == '__main__':
    asyncio.run(inspect_scroll())
