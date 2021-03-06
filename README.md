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
- [Convention](https://spoqa.github.io/2012/08/03/about-python-coding-convention.html)  
python 코딩 스타일 가이드
- [Asterisk](https://mingrammer.com/understanding-the-asterisk-of-python/)  
python에서 * 사용법 이해하기
- [Python 블로그](https://beomi.github.io)  
Python 과 pyspark 등 다양한 지식을 적어놓은 사이트
- [Python 설정 파일](https://mingrammer.com/ways-to-manage-the-configuration-in-python/)  
Python에서 설정 파일에 관한 글
- [Try Exception](https://docs.python.org/3/tutorial/errors.html)  
Python에서 Try Except 사용법

#### TODO
- [x] XlsxWriter를 이용해서 메타데이터를 파일을 만든는 코드를 만들어봅시다.  
안의 내용물은 아무것이나 해도되고 메타데이터 포멧대로 excel 만들어주는 코드를 작성해주시면 됩니다.  
아래 링크들 참고해 주시면 되겠습니다 :)  
[Tutorial1](https://xlsxwriter.readthedocs.io/tutorial01.html)  
[Tutorial2](https://xlsxwriter.readthedocs.io/tutorial02.html)  
[Format Class](https://xlsxwriter.readthedocs.io/format.html)  

- [x] `BeautifulSoup4`를 이용해 간단히 가져올 수 있는 정보들 찍어내기.  
[Navigating Tree](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree)

- [x] 크롤러를 class로 만들어서 코드에 적용해보기.

- [x] Selenium을 이용해서 수정여부 및 검증결과 가져오기.

- [ ] Selenium을 이용해서 댓글수 & 반응 가져오기

#### data 정리
- 쉽게 가져올 수 있는 것  
  서버번호, 토픽, 팩트유형, 기타성격, 발언주체, 발언대상, 발언내용, 사실/기타 주제, 대상, 내용,  
  최초등록시간, 검증결과 수정시간, 검증결과 수정이유, 검증내용, 최초검증결과, 검증결과수정여부, 수정검증결과,  
  검증기사URL, 
- 약간의 작업이 필요한 것  
  검증팩트의 영향력, 검증방식, 검증기사제목, 팩트검증 기사영향력, 검증근거&출처, 검증근거&출처URL

#### 사소한 팁
- `worksheet.set_column` 이란 함수에서 width 인자를 넘겨 칸의 크기를 조정할 수 있다.  
```
worksheet.set_column(0, 0, 20)   # Column  A   width set to 20.  
worksheet.set_column(1, 3, 30)   # Columns B-D width set to 30.  
worksheet.set_column('E:E', 20)  # Column  E   width set to 20.  
worksheet.set_column('F:H', 30)  # Columns F-H width set to 30.
```   
- `selenium`에서 웹에서 클릭 등 작업을 하고 난 뒤 바뀐 내용을 크롤링 하고자 할 때,  
  `time.sleep(2)` 와 같은 코드로 2초 정도(컴퓨터 사양에 따라 다름) 기다린 다음,  
  웹에서 내용이 바뀔 만큼 충분히 기다려 주고나서 크롤링 해야한다. 

#### 일지
- 2019/01/06  
Pandas 와 XlsxWriter Tutorial 링크를 올림.  
팩트체크 메타데이터를 크롤링하여 만들어 주는 일 자동화로 큰 프로젝트를 설정함.
- 2019/01/13  
메타데이터의 기본 틀 만듦.  
크롤러로 기본적인 정보들 가져오는 것 시작.  
- 2019/01/26  
클래스로 만들기 시작
- 2019/02/02  
class로 만든거 코드 리뷰 밑 리팩터링  
selenium으로 크롤링하기
- 2019/02/09  
headless chrome 으로 교체  
서버 번호 시작 끝 지정 하는 것  
설정 파일 만들기   
