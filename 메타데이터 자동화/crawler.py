from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import time

class Crawler(object):

    def __init__(self, i):
        self.Server_number = i
        self.Topic = ''
        self.Check_category = ''
        self.Speaker = ''
        self.Comment = ''
        self.Media = ''
        self.Time = ''
        self.Modification_time = ''
        self.Modification_reason = ''
        self.Details = ''
        self.Article_url = ''
        self.Article_title = ''
        self.Modi_result = ''
        self.Org_result = ''
        self.Is_modified = ''
        self.base_url = "http://factcheck.snu.ac.kr/v2/facts/" + str(i)

    def topic_and_type(self):

        with urllib.request.urlopen(self.base_url) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")
            # 토픽 & 검증 유형
            category = soup.find("div", class_="fcItem_detail_bottom")
            categories = category.find_all("li")
            self.Topic = categories[0].text 
            self.Check_category = categories[1].text
            # print(categories[0].text) # 값 저장해서 main에서 출력하는 식으로
            # print(categories[1].text)
    
    def speaker(self):

        with urllib.request.urlopen(self.base_url) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")
            # 발언주체
            find_speaker = soup.find("p", class_="name")
            self.Speaker = find_speaker.text # 값 저장해서 main에서 출력하는 식으로 

    def comment(self):
        
        with urllib.request.urlopen(self.base_url) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")
            # 발언내용
            find_comment = soup.find("div", class_="fcItem_detail_li_p")
            self.Comment = find_comment.a.text # 값 저장해서 main에서 출력하는 식으로

    def media(self):
        media_list = ['', '한국경제', '아시아경제', '뉴시스', '아이뉴스24', '뉴스1', '머니투데이', 
             '', '세계일보', '오마이뉴스', 'TV조선', 'MBC', '', '한국일보', 'KBS', '', 'MBN', 
             '조선일보', '매일경제', '서울신문', 'SBS', '중앙일보', 'JTBC', 'YTN', '동아사이언스',
             '뉴스톱', '문화일보', '이데일리', '전북일보', '노컷뉴스', '연합뉴스']

        with urllib.request.urlopen(self.base_url) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")   
            # 참여 언론사
            raw_media_url = soup.find("div", class_="checked_by")
            media_url = raw_media_url.img
            media_url = media_url["src"]
            for i in range(0, len(media_list)):
                if 'logo_image/' + str(i) + '/' in media_url:
                    self.Media = media_list[i]
                    # print(media_list[i]) # 값 저장해서 main에서 출력하는 식으로

    def time(self):

        with urllib.request.urlopen(self.base_url) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")    
        # 최초 등록 시간, 검증결과 수정 시간
        time = soup.find("div", class_="reg_date")
        time_text = time.text.split('\n')
        times = [a.strip() for a in time_text if a != ''] # 이 코드 이해하기
        if(len(times) == 1):
            self.Time = times[0]
            # print(times[0]) # 값 저장해서 main에서 출력하는 식으로
        else:
            self.Time = times[1] # 값 저장해서 main에서 출력하는 식으로
            self.Modification_time = times[-2] # 값 저장해서 main에서 출력하는 식으로
            self.Modification_reason = times[-1] # 값 저장해서 main에서 출력하는 식으로
    
    def details(self):

        with urllib.request.urlopen(self.base_url) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")        
            # 검증 내용
            summary = soup.find("div", class_="vf_exp exp fr-view")
            self.Details = summary.text # 값 저장해서 main에서 출력하는 식으로

    def url_and_title(self):

        with urllib.request.urlopen(self.base_url) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")
            # 검증기사URL & 검증기사제목
            article_url = soup.find("p", class_="vf_article")
            self.Article_url = article_url.a["href"]
            self.Article_title = article_url.a.text

    def result(self):

        driver = webdriver.Chrome('/Users/jinyoung/Desktop/chromedriver_win32/chromedriver.exe')
        driver.implicitly_wait(5)
        driver.get(self.base_url)        

        try:
            driver.find_element_by_xpath('//*[@class="reg_date"]/p/a').click()
            self.Modi_result = driver.find_element_by_xpath('//*[@class="meter-label"]').text
            driver.find_elements_by_xpath('//*[@class="reg_date"]/ul/li')[-1].click()
            time.sleep(5)
            self.Org_result = driver.find_element_by_xpath('//*[@class="meter-label"]').text
            self.Is_modified = 'yes'

        except:
            self.Org_result = driver.find_element_by_xpath('//*[@class="meter-label"]').text
            self.Is_modified = 'no'