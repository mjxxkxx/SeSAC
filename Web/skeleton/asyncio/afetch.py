import asyncio
import aiohttp

async def afetch(url, session):

    response = await session.get(url)

    if response.status == 200:
        return await response.tex()

def main():
    urls = [...]
    tasks = [afetch(url, session) for url in urls]
    
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
