##### WINTER with Jinyoung & Koo
#### 참고 링크
- [XlsxWriter](https://xlsxwriter.readthedocs.io/#)  
Pandas와 함께 같이 쓸 수 있는 Excel 작성하는 라이브러리
- [Pandas](http://pandas.pydata.org/pandas-docs/version/0.15/tutorials.html)  
Pandas는 데이터 분석시에 사용하는 라이브러리
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
크롤링 할 때 사용하는 라이브러리
- [새글 알림 봇](https://beomi.github.io/2017/04/20/HowToMakeWebCrawler-Notice-with-Telegram/)  
telegram에 새글이 뜨면 알림을 주는 봇을 만드는 글  
- [Enumerate](http://book.pythontips.com/en/latest/enumerate.html)  
for문을 할 때 index와 value가 같이 나오게 할 수 있는 함수

#### TODO
- [x] XlsxWriter를 이용해서 메타데이터를 파일을 만든는 코드를 만들어봅시다.  
안의 내용물은 아무것이나 해도되고 메타데이터 포멧대로 excel 만들어주는 코드를 작성해주시면 됩니다.  
아래 링크들 참고해 주시면 되겠습니다 :)  
[Tutorial1](https://xlsxwriter.readthedocs.io/tutorial01.html)  
[Tutorial2](https://xlsxwriter.readthedocs.io/tutorial02.html)  
[Format Class](https://xlsxwriter.readthedocs.io/format.html)  

- [ ] `BeautifulSoup4`를 이용해 간단히 가져올 수 있는 정보들 찍어내기.  
[Navigating Tree](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree)

- [ ] 크롤러를 class로 만들어서 코드에 적용해보기.

#### data 정리
- 쉽게 가져올 수 있는 것  
  서버번호, 토픽, 팩트유형, 기타성격, 발언주체, 발언대상, 발언내용, 사실/기타 주제, 대상, 내용,  
  최초등록시간, 검증결과 수정시간, 검증결과 수정이유, 검증내용, 최초검증결과, 검증결과수정여부, 수정검증결과,  
  검증기사URL, 
- 약간의 작업이 필요한 것  
  검증팩트의 영향력, 검증방식, 검증기사제목, 팩트검증 기사영향력, 검증근거&출처, 검증근거&출처URL

#### 일지
- 2019/01/06  
Pandas 와 XlsxWriter Tutorial 링크를 올림.  
팩트체크 메타데이터를 크롤링하여 만들어 주는 일 자동화로 큰 프로젝트를 설정함.
- 2019/01/13  
메타데이터의 기본 틀 만듦.  
크롤러로 기본적인 정보들 가져오는 것 시작.  
