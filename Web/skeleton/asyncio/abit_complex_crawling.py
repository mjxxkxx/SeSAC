import asyncio 
import aiohttp
import requests 
from bs4 import BeautifulSoup
from time import time, sleep
'''
1. async def async_task(task_num, duration): defines an asynchronous function using the async keyword.
It uses await asyncio.sleep(duration) instead of time.sleep(duration). 
This allows other tasks to run while this task is "sleeping".

2. async def main(): the main asynchronous function that creates and manages the tasks.

3. asyncio.create_task() is used to schedule the execution of a coroutine. It returns a Task object.

4. await task1, await task2, await task3 waits for each task to complete.

5. async def gather_main(): an alternative main function that uses asyncio.gather().

6. asyncio.gather() runs the given coroutines concurrently and waits for all of them to complete.

7. asyncio.run(main()): runs the main() coroutine and manages the asyncio event loop.

async/await: These keywords are used to define and work with coroutines (asynchronous functions).
asyncio.sleep(): An asynchronous version of time.sleep().
asyncio.create_task(): Schedules a coroutine to run soon.
asyncio.gather(): Runs awaitables concurrently.
asyncio.run(): Runs the top-level entry point for asyncio programs.
'''
def crawl_press_names_and_codes():
    """Make the dict that have press code as key, and press name as value. Crawl from https://media.naver.com/channel/settings. 
    """
    begin = time()
    url = 'https://media.naver.com/channel/settings'
    code2name = {}

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        for li in soup.find_all('li', {'class':'ca_item _channel_item'}):
            press_name = li.find('div', {'class':'ca_name'}).text
            press_code = li['data-office']
            code2name[press_code] = press_name
            
    else:
        assert False 

    end = time()

    return code2name

async def afetch_journalist_list(press_code, session):
    url = f'https://media.naver.com/journalists/whole?officeId={press_code}'
    print(f'started crawling {url} at {time()}')

    response = await session.get(url) 
    journalist_list = []
    
    if response.status == 200:
        text = await response.text() 
        soup = BeautifulSoup(text, 'html.parser')

        for li in soup.find_all('li', {'class':'journalist_list_content_item'}):
            info = li.find('div', {'class':'journalist_list_content_title'})
            a = info.find('a')
            journalist_name = a.text.strip('기자')
            journalist_link = a['href']
            journalist_list.append((journalist_name, journalist_link))
            
        print(f'ended crawling {url} at {time()}')

        return journalist_list

async def acrawl_journalist_info_pages(code2name):
    begin = time()

    session = aiohttp.ClientSession()
    
    tasks = [afetch_journalist_list(press_code, session) for press_code in code2name]
    await asyncio.gather(*tasks)

    end = time()

    print(end - begin)

if __name__ == '__main__':
    code2name = crawl_press_names_and_codes()
    asyncio.run(acrawl_journalist_info_pages(code2name))