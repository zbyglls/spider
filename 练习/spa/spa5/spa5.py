import httpx
import asyncio


async def get_id(url):
    async with httpx.AsyncClient() as client:
        res = await client.get(url, timeout=None)
        id = [_['id'] for _ in res.json()['results']]
        return id


async def get_detail(url):
    async with httpx.AsyncClient() as client:
        res = await client.get(url, timeout=None)
        print(url)
        print(res.json())


async def main():
    for page in range(1, 503):
        offset = (page - 1) * 18
        url = f'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
        id = await get_id(url)
        urls = [f'https://spa5.scrape.center/api/book/{_}/' for _ in id]
        for _ in urls:
            await get_detail(_)


if __name__ == '__main__':
    asyncio.run(main())
