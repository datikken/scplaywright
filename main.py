import os
import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

HOME_PAGE = os.getenv('HOME_PAGE')

async def getHref(link):
    return await link.get_attribute('href')

async def main():
    async with async_playwright() as p:
        browser_type = p.chromium
        browser = await browser_type.launch()
        page = await browser.new_page()
        await page.goto(f'{HOME_PAGE}')
        els = await page.query_selector_all('a')
        links = [await getHref(link) for link in els]
        print(links)
        await page.screenshot(path=f'example-{browser_type.name}.png')
        await browser.close()


asyncio.run(main())
