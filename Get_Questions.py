# coding:utf-8

import re
import json
from bs4 import BeautifulSoup
from Get_Html import Get_Html


class Get_Questions:

    def __init__(self,str_html):
        self.str_html = str_html
        # 单选题 CSS选择器配置列表
        self.dan_xuan = ['div#timu table#GridView1 span.title','div#timu table#GridView1 table.t1 span']
        # 多选题 CSS选择器配置列表
        self.duo_xuan = ['div#timu table#GridView2 span.title','div#timu table#GridView2 table.t1 span']
        # 判断题 CSS选择器配置列表
        self.pan_duan = ['div#timu table#GridView3 span.title','div#timu table#GridView3 table#t3 span']


    # 解析单个html网页，返回题目列表
    def parse_html(self):
        return self.get_questions_list('danxuan') + self.get_questions_list('duoxuan') + self.get_questions_list('panduan')


    # 解析不同题型的数据，返回题型对应的试题列表
    def get_questions_list(self,type):
        soup = BeautifulSoup(self.str_html.content,'lxml')
        if type == 'danxuan':
            selector_title, selector_main = self.dan_xuan
        if type == 'duoxuan':
            selector_title, selector_main = self.duo_xuan
        if type == 'panduan':
            selector_title, selector_main = self.pan_duan

        title = soup.select(selector_title)[0].get_text()
        elements = soup.select(selector_main)

        questions =  [title] + self.parse_question(elements)

        return questions
        

    # 遍历span标签，解析题号，题干，答案及选项
    def parse_question(self,elements):
        temp = []
        question = dict()
        for ele in elements:
            text = str(ele.get_text())
            if self.is_number(text):
                # 根据题号判断是否遍历完一题的内容（题号，题干，答案及选项）
                if len(question) > 0:
                   # 由于question是实例，不是不可变的对象，因此question值变化时，列表中的字典的值也会变
                   temp.append(question.copy())
                question['num'] = text
                options = []
            elif self.is_question(text):
                if len(question) > 0:
                    question['item'] = text
            elif self.is_answer(ele):
                if len(question) > 0:
                    question['answer'] = text
            elif self.is_options(text):
                if len(question) > 0:
                    options.append(text)
                    question['options'] = options
        # 将最后一次解析的结果放到列表中
        if len(question) > 0:
            temp.append(question.copy())

        return temp


    # 判断是否是题号
    def is_number(self,text):
        num = re.findall(r'\d{1,2}、',str(text))
        if len(num) > 0:
            return True
        else:
            return False 


    # 判断是否是问题题干
    def is_question(self,text):
        if '?' in text or '。' in text or '？' in text:
            return True
        else:
            return False 
    

    #判断是否是答案
    def is_answer(self,element):
        if 'style' in str(element):
            # style="color:Red;" 即为答案
            if element['style'] == 'color:Red;':
                return True
            else:
                return False 
        else:
            return False 
    

    # 判断是否是选择题的选项
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
# print(Get_Questions(html).parse_html())