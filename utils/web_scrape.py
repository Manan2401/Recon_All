import asyncio
import aiohttp
import time
import random
from bs4 import BeautifulSoup
from helper import printer
from utils.randomuser import users


class Scrape:
    """
    Scrapes links from a given website.

    :param url: The website url.
    """
    def __init__(self, url):
        try:
            printer.info(f"Trying to scrape links from '{url}'...")
            start_time = time.time()
            asyncio.run(self.scrape_links(url))
            end_time = time.time()
            printer.success(f"Scraping complete. Total time: {end_time - start_time:.2f} seconds.")
        except Exception as e:
            printer.error(f"Error: {e}")

    @staticmethod
    async def fetch(session, url):
        headers = {"User-Agent": random.choice(users)}
        async with session.get(url, headers=headers) as response:
            return await response.text()

    @staticmethod
    async def parse_links(content):
        soup = BeautifulSoup(content, "html.parser")
        links = soup.find_all("a")
        return [(link.get("href"), link.text) for link in links]

    async def scrape_links(self, url):
        async with aiohttp.ClientSession() as session:
            html_content = await self.fetch(session, url)

            # TODO This part can be further improved by using ThreadPoolExecutor to parse links concurrently.
            links = await self.parse_links(html_content)

            count = 0
            for href, text in links:
                count += 1
                printer.success(f"found {count} link(s): {href} - {text}")
