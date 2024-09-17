import requests 
from bs4 import BeautifulSoup

def crawl_breaking_news_list():
    news_url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0014907888'

    response = requests.get(news_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        td = soup.find('td', {'class':'content'})
        for li in td.find_all("li"):
            try:
                if li['data-comment'] is not None:
                    a = li.find('a')
                    link = a['href']
                    text = a.text.strip()
                    print(f"{text}\n{link}\n")

            except KeyError:
                pass


def crawl_ranking_news():
   
    ranking_url = 'https://news.naver.com/main/ranking/popularDay.naver'

    response = requests.get(ranking_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    '''
    1) 언론사 이름 : a href = 링크 class = "rankingnews_box_head nclicks('RBP.rnkpname')
    2) 기사 이름 : div clss = "list_content" 
     tag 가 a / href / class = "rankingnews_box_head nclicks('RBP.rnknws')"
    '''
    divs = soup.find_all('div', {'class':'rankingnews_box'})

    for div in divs:
        strong = div.find('strong',{'class':'rankingnews_name'})
        if strong is not None:
            text = strong.text.strip()
            print(text)
            for li in div.find_all('li'):
                try:
                    if li is not None:
                        a = li.find('a')
                        if a is not None:
                            link = a['href'].strip()
                            text = a.text.strip()
                            print(f'{text}\n{link}\n')

                except KeyError:
                    pass
  

if __name__ == '__main__':
    # crawl_breaking_news_list()
    crawl_ranking_news()
