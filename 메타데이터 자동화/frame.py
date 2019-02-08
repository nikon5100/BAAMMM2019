import xlsxwriter

class Frame(object):

    def __init__(self, **kwargs):
        self.Server_number = kwargs.get('server_number', '')
        self.Topic = kwargs.get('topic', '') # 이게 불러오는게 topic 없으면 빈 스트링 집어넣으라는 얘기
        self.Check_category = kwargs.get('check_category', '')
        self.Speaker = kwargs.get('speaker', '')
        self.Comment = kwargs.get('comment', '')
        self.Media = kwargs.get('media', '')
        self.Time = kwargs.get('time', '')
        self.Modification_reason = kwargs.get('modification_reason', '')
        self.Modification_time = kwargs.get('modification_time', '')
        self.Details = kwargs.get('details', '')
        self.Article_title = kwargs.get('article_title', '')
        self.Article_url = kwargs.get('article_url', '')
        self.Modi_result = kwargs.get('modi_result', '')
        self.Org_result = kwargs.get('org_result', '')
        self.Is_modified = kwargs.get('is_modified', '')

        self.fact_descriptions = (
            ['팩트', '서버번호', self.Server_number],
            ['', '뱃지번호', ''],
            ['', '토픽(정치, 경제 등)', self.Topic],
            ['', '테마(19대 대선, 새정부 등)', ''],
            ['', '팩트유형(검증 유형)', self.Check_category],
            ['', '기타성격', ''],
            ['', '팩트발생시간', ''],
            ['', '발언주체', self.Speaker],
            ['', '발언대상', ''],
            ['', '발언내용', self.Comment],
            ['', '사실/기타주체', ''],
            ['', '사실/기타대상', ''],
            ['', '사실/기타내용', ''],
            ['', '검증팩트의 영향력', '1.(네이버 실시간 검색어)\n2.(SNU 게시일 기준 기사 수)'],
        )

        self.fact_check_descriptions = (
            ['팩트체크', '참여언론사', self.Media],
            ['', '최초등록시간', self.Time],
            ['', '검증내용', self.Details],
            ['', '검증방식', ''],
            ['', '검증근거/출처', ''],
            ['', '검증근거/출처 URL', ''],
            ['', '검증기사제목', self.Article_title],
            ['', '검증기사URL', self.Article_url],
            ['', '최초검증결과', self.Org_result],
            ['', '검증결과수정여부', self.Is_modified],
            ['', '수정검증결과', self.Modi_result],
            ['', '검증결과 수정시간', self.Modification_time],
            ['', '검증결과 수정이유', self.Modification_reason],
            ['', '팩트검증 기사영향력', '(댓글수)\n(이모티콘 평가 수)'],                           
        )

        # Create a workbook and add a worksheet.
      
        self.workbook = xlsxwriter.Workbook('meta_data.xlsx')
        self.worksheet = self.workbook.add_worksheet()
    
        # Create a add format to cell

        self.cell_format_list = []
        color_list = ['#d9d9d9', '#ffe599', '#fff2cc', '#ffffff','#ea9999', '#fce5cd', '#ffffff']

        for i in range(0, len(color_list)):
            self.cell_format_list.append(self.workbook.add_format())
            self.cell_format_list[i].set_bg_color(color_list[i])
            self.cell_format_list[i].set_border(1)

    def header(self):
        # Write some data headers.
        self.worksheet.write('A1', '메타데이터 종류', self.cell_format_list[0])
        self.worksheet.write('B1', '모니터링 담당자', self.cell_format_list[0])
        self.worksheet.write('C1', '', self.cell_format_list[0])

    def color_and_data_wirte(self):
        # Start from the first cell. Rows and columns are zero indexed.
        row = 2
        col = 0
        col_alphabets = ['A', 'B', 'C']

        for description in self.fact_descriptions: # 이중포문으로 칼럼 확장시 자동으로 추가될 수 있게 하자.
            for i in range(0, len(description)):
                self.worksheet.write(col_alphabets[i]+str(row), description[i], self.cell_format_list[i+1])
            row += 1

        for description in self.fact_check_descriptions: 
            for i in range(0, len(description)):
                self.worksheet.write(col_alphabets[i]+str(row), description[i], self.cell_format_list[i+4])
            row += 1

        #    worksheet.write(row, col,     data_kind)
        #    worksheet.write(row, col + 1, category)
        #    worksheet.write(row, col + 2, content)

    def merge(self):

        fact_merge_format = self.workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#ffe599'})

        fact_check_merge_format = self.workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#ea9999'})    

        self.worksheet.merge_range('A2:A15', '팩트', fact_merge_format)
        self.worksheet.merge_range('A16:A29', '팩트체크', fact_check_merge_format)

    def close(self):
        self.workbook.close()

