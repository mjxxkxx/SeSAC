from playwright.async_api import async_playwright
from time import time, sleep
import asyncio

async def ticket_id(page, search_keyword = '1772651410'):
    search = await page.wait_for_selector('#txtMember') # query 속성을 가진 tag가 일정 시간 이상 응답이 없을 경우 TimeOut Error
    await search.type(search_keyword)

async def ticket_pwd(page, search_keyword = 'Queenmj1012!'):
    search = await page.wait_for_selector('#txtPwd') # query 속성을 가진 tag가 일정 시간 이상 응답이 없을 경우 TimeOut Error
    await search.type(search_keyword)

async def login_click(page):
    await ticket_id(page)
    await ticket_pwd(page)
    execute_login = await page.wait_for_selector('.btn_login') 
    await execute_login.click()
    
    # # 비회원 로그인 버튼 찾기 및 클릭
    # execute_login = await page.wait_for_selector('.box_rig') 
    # await execute_login.click()
    
    # 페이지 로딩 대기
    await page.wait_for_selector('#contents')
    
    # 출발지 입력
    await page.fill('#start', '천안아산')

    # 도착지 입력
    await page.fill('[name="txtGoEnd"]', '서울') 

    await page.select_option('#s_year', '2024')
    await page.select_option('#s_month', '09')
    await page.select_option('#s_day', '16') 
    await page.select_option('#s_hour', '16')  

    # 조회
    execute_browse = await page.wait_for_selector('.btn_inq') 
    await execute_browse.click()

    # # 예매 선택 버튼 클릭
    # await page.evaluate("document.querySelector('#btnRsv5_0').click()")
    
    # choose_train = await page.wait_for_selector('#btnRsv5_0')
    
    # await choose_train.click()
    sleep(1)
    # await page.evaluate('''(() => {
    # select_seat = document.querySelector('img[name="btnRsv5_0"]');
    # select_seat.click();
    # })();''')

    await page.evaluate('''(() => {
        infochk(2,0);
    })();''')
    # 잠시 대기 (10초)
    from code import interact
    interact(local = locals())
    # await asyncio.sleep(200)
    sleep(10)
        
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = False)
        context = await browser.new_context()
        page = await browser.new_page()
        
        await page.goto('https://www.letskorail.com/korail/com/login.do')
        await login_click(page)

if __name__ == '__main__':
    asyncio.run(main())