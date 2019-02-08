# from frame import Frame
from crawler import Crawler
from frame import Frame

# 데이터 수집

for number in range(0, 1328):
    crawler = Crawler(number)
    crawler.topic_and_type()
    crawler.speaker()
    crawler.comment()
    crawler.media()
    crawler.time()
    crawler.details()
    crawler.url_and_title()
    crawler.result()

# Excel 파일에 데이터 넣기
    # keyword argument
    frame = Frame(
        server_number=crawler.Server_number, # crawler에서 받아온 인자를 다시 키워드 변수로 바꿔서 frame에 넣어주기
        topic=crawler.Topic, 
        check_category=crawler.Check_category, 
        speaker=crawler.Speaker, 
        comment=crawler.Comment, 
        media=crawler.Media, 
        time=crawler.Time,
        modification_time=crawler.Modification_time,
        modification_reason=crawler.Modification_reason,
        detail=crawler.Details,
        article_url=crawler.Article_url,
        article_title=crawler.Article_title
        modi_result=crawler.Modi_result
        org_result=crawler.Org_result
        is_modified=crawler.Is_modified
    )

    frame.header()
    frame.color_and_data_wirte()
    frame.merge()
    frame.close()

    
