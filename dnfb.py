import asyncio
import aiohttp

from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

BASE_URL = "https://www.youtube.com/" 
HEADERS = {"User-Agent": UserAgent(browsers="chrome")}


async def main():
    async with aiohttp.ClientSession() as session: 
        async with session.get(BASE_URL) as response:
            r = await aiohttp.StreamReader.read(response.content) 
            soup = BS(r, "html.parser")
            items = soup.find_all("div", class_="style-scope ytd-rich-grid-row") 
            print("+")
            print(items)
            for item in items: 
                print("+")
                title = item.find("yt-formatted-string", {"class": "style-scope ytd-rich-grid-media"})
                print(title)

if __name__ == '__main__': 
    loop = asyncio.get_event_loop() 
    loop.run_until_complete(main()) 