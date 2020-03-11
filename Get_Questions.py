# coding:utf-8

from bs4 import BeautifulSoup
from Get_Html import Get_Html


class Get_Questions:
    def __init__(self,str_html):
        self.str_html = str_html

    def parse_html(self):
       soup = BeautifulSoup(self.str_html.content,'lxml')

       #单选题
       title_danxuan = soup.select('div#timu table#GridView1 span.title')[0].get_text()
       self.questions['type']
       print(title_danxuan,type(title_danxuan))
       elements_danxuan = soup.select('div#timu table#GridView1 table.t1 span')
       for ele in elements_danxuan:
           print(ele.get_text())


       #多选题
       title_duoxuan = soup.select('div#timu table#GridView1 span.title')[0].get_text()
       print(title_duoxuan)
       elements_duoxuan = soup.select('div#timu table#GridView2 table.t1 span')
       for ele in elements_duoxuan:
           print(ele.get_text())

       #判断题
       title_panduan = soup.select('div#timu table#GridView3 span.title')[0].get_text()
       print(title_panduan)
       elements_panduan = soup.select('div#timu table#GridView3 table#t3 span')
       for ele in elements_panduan:
           print(ele.get_text())



    def is_question(self,text):
        if '（    ）' in text and '。' in text:
            return True
        else:
            return False 
    
    def is_answer(self,text):
        # style="color:Red;" 即为答案
        if text == 'color:Red;'
            return True
        else:
            return False 
    
    # 选择题选项
    def is_options(self,text):
        if 'A' in text:
            return True
        elif 'B' in text:
            return True
        elif 'C' in text:
            return True
        elif 'D' in text:
            return True
        elif 'E' in text:
            return True
        elif 'F' in text:
            return True
        else:
            return False 



# test code
# html = Get_Html().get_a_html(1,1)
# Get_Questions(html).parse_html()