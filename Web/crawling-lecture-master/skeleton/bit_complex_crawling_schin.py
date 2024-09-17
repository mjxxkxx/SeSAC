import requests 
from bs4 import BeautifulSoup
import os
from time import time, sleep
import pickle

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

def fetch_journalist_list(press_code):
    url = f'https://media.naver.com/journalists/whole?officeId={press_code}'
    print(f'started crawling {url} at {time()}')

    response = requests.get(url)
    journalist_list = [] 
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        for li in soup.find_all('li', {'class':'journalist_list_content_item'}):
            info = li.find('div', {'class':'journalist_list_content_title'})
            a = info.find('a')
            journalist_name = a.text.strip('기자')
            journalist_link = a['href']
            journalist_list.append((journalist_name, journalist_link))

        print(f'ended crawling {url} at {time()}')
        return journalist_list

def crawl_journalist_info_pages(code2name):
    """Accepts press code - press name dict, and return dict having press code as key, and 2-tuple of (press name, listof 2-tuple containing journalist name and their link) as value. 

    For now, you DO NOT have to crawl all journalists; for now, it's impossible. 
    Crawl from https://media.naver.com/journalists/. 
    """
    def crawl_journalist_info(link):
    """Make a Journalist class instance using the information in the given link. 
    """
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        profile_head = soup.find('div', {'class' : 'media_reporter_basic_text'})

        press_code = profile_head.find('a')['href'].split('/')[-1]
        journalist_name = profile_head.find('h2', {'class': 'media_reporter_basic_name'}).text

        award_div = soup.find('div', {'class':'media_reporter_profile_award'})
        award_dict = {}
        school_list = []
        
        for award in award_div.find_all('div', {'class' : 'media_reporter_award_div'}):
            award_category = award.find('h4', {'class': 'media_reporter_award_category'}).text
            award_list = award.find('ul', {'class' : 'media_reporter_award_list'})

            if award_category != '학력':
                award_lst = []
                for award_item in award_list.find_all('li', {'class' : 'media_reporter_award_item'}):
                    award_year = award_item.find('em', {'class' : 'media_reporter_award_year'}).text.strip() 
                    award_name = award_item.find('ul', {'class' : 'media_reporter_award_name'}).text.strip()
                    award_lst.append((award_year, award_name))
                award_dict[award_category] = award_lst
            else:
                for school_item in award_list.find_all('li', {'class' : 'media_reporter_award_item'}):
                    graduation_year = school_item.find('em', {'class' : 'media_reporter_award_year'}).text.strip() 
                    school_name = school_item.find('ul', {'class' : 'media_reporter_award_name'}).text.strip()
                    
                    school_list.append((graduation_year, school_name))
            
        no_of_subscribers = requests.get(f'https://media.naver.com/myfeed/getFeedCount?channelKeys=JOURNALIST_{link.split("/")[-1]}')
        
        if no_of_subscribers.status_code == 200:
            no_of_subscribers = int(json.loads(no_of_subscribers.text)['result'][0]['count'])
        else:
            no_of_subscribers = 0
    
        subscriber_age_statistics = {}
        age_statistics_chart = soup.find('dl', {'class' : 'group_barchart'})

        for age_category in age_statistics_chart.find_all('div', {'class' : 'group'}):
            age = age_category.find('dt').text.strip() 
            value = age_category.find('span', {'class': 'percent'}).text.strip().strip('%')
            subscriber_age_statistics[age] = value 
        
        gender_statistics = soup.find('div', {'class' : 'group_piechart _gender_chart_area'}).text.strip().split()
        male_ratio = gender_statistics[1].strip('%')
        female_ratio = gender_statistics[3].strip('%')

        subscriber_gender_statistics = {'male' : male_ratio, 'female' : female_ratio}

        article_list = []

        article_list_ul = soup.find_all('ul', {'class' : 'press_edit_news_list'})
        
        for article_list_set in article_list_ul:
            for article in article_list_set.find_all('li'):
                a = article.find('a')
                span = article.find('span', {'class' : 'press_edit_news_title'})
                article_list.append((a['href'], span.text))
        

    return Journalist(name = journalist_name, 
                    press_code = press_code,
                    career_list = award_dict, 
                    graduated_from = school_list, 
                    no_of_subscribers = no_of_subscribers, 
                    subscriber_age_statistics = subscriber_age_statistics, 
                    subscriber_gender_statistics = subscriber_gender_statistics, 
                    article_list = article_list, 
           )


class Journalist:
    def __init__(self, name, press_code, 
                career_list, 
                graduated_from, 
                no_of_subscribers, 
                subscriber_age_statistics, 
                subscriber_gender_statistics, 
                article_list):
        self.name = name 
        self.press_code = press_code 
        self.career_list = career_list
        self.graduated_from = graduated_from
        self.no_of_subscribers = no_of_subscribers
        self.subscriber_age_statistics = subscriber_age_statistics
        self.subscriber_gender_statistics = subscriber_gender_statistics

        self.article_list = article_list 

def crawl_journalist_info(link):
    """Make a Journalist class instance using the information in the given link. 
    """
    '''
    press name  
    statstics
    num of journal
    major
    '''
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        profile  = soup.find('div', {'class':'journalist_profile_body'})
        press_name = profile.find('span',   {'class':'media_reporter_basic_press_txt'}).text.strip()
        name = profile.find('h2', {'class':'media_reporter_basic_name'}).text.strip()
        no_of_subscribers = profile.find('em', {'class':'media_reporter _popularity_subscribenum _journalist_subscirbe_count _txt'}).text.strip()
        cheer_count = profile.find('em', {'class':'u_cnt _count _journalist_cheer_Count'}).text.strip()

        print(f'{press_name}\n{name}\n 구독: {no_of_subscribers}|응원: {cheer_count}')

        career_list = []

        for div in soup.find('div', {'class':'media_reporter _award_div'}):
            for li in div.find_all('li', {'class':'media_reporter_award_item'}):
                career_year = li.find('em', {'class':'media_reporter _award_year'}).text.strip()
                career_content = li.find('li').text.strip()
                career_list.append((career_year, career_content))

        award_list = []

        for div in soup.find('div', {'class':'media_reporter _award_div'}):
            for li in div.find_all('li', {'class':'media_reporter_award_item'}):
                award_year = li.find('em', {'class':'media_reporter _award_year'}).text.strip()
                award_content = li.find('li').text.strip()
                award_list.append((award_year, award_content))

        print('이력 |\t')
        for career_year, career_content in career_list:
            print(f'{career_year} {career_content}')

        print('수상 |\t')
        for award_year, award_content in award_list:
            print(f'{award_year} {award_content}')    

if __name__ == '__main__':
    code2info_pickle = 'code2info.pickle'

    if code2info_pickle in os.listdir():
        begin = time()
        code2info = pickle.load(open(code2info_pickle, 'rb'))    
        end = time()
        print(f'{end - begin} sec passed for unpickling')
    else:
        begin = time()
        code2name = crawl_press_names_and_codes()
        code2info = crawl_journalist_info_pages(code2name)
        pickle.dump(code2info, open(code2info_pickle, 'wb+'))
        end = time()
        print(f'{end - begin} sec passed for execution and pickling')

    code2name = crawl_press_names_and_codes()
    crawl_journalist_info_pages(code2name)

    for code, (press_name, journalist_list) in code2info.items():
        for journalist_name, link in journalist_list:
            j = crawl_journalist_info(link)
            assert j.name == journalist_name
