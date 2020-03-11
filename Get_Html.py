# coding:utf-8

import os
import requests
from bs4 import BeautifulSoup

class Get_Html:
    def __init__(self):
        self.save_path = r"D:\my_python_code\web_spider\temp"
        self.url = 'http://zjzx.zjnu.edu.cn/test/Default.aspx?cid={:d}&pid={:d}'
        self.viewstate = "__VIEWSTATE"
        self.eventvalidation = "__EVENTVALIDATION"
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}


    # 发送get请求
    def get_request(self,cid,pid):
            return requests.get(self.url.format(cid,pid),headers=self.headers)


    #发送post请求
    def post_request(self,cid,pid,key,strhtml):
            v,e = self.get_value(strhtml)
            if key == 'DANXUAN':
                form_data = {'__VIEWSTATE':v,
                             '__EVENTVALIDATION':e,
                             'Button1':'提交并查看单选题答案'}
            elif key == 'DUOXUAN':
                form_data = {'__VIEWSTATE':v,
                             '__EVENTVALIDATION':e,
                             'Button2':'提交并查看多选题答案'}
            elif key == 'PANDUAN':
                form_data = {'__VIEWSTATE':v,
                             '__EVENTVALIDATION':e,
                             'Button3':'提交并查看判断题答案'}
            return requests.post(self.url.format(cid,pid),headers=self.headers,data=form_data)


    #根据请求返回的html获得__VIEWSTATE，__EVENTVALIDATION值，用于post请求题目答案
    def get_value(self,strhtml):
        soup = BeautifulSoup(strhtml.content,'lxml')
        v = soup.select('#__VIEWSTATE')[0]['value']
        e = soup.select('#__EVENTVALIDATION')[0]['value']
        return v, e


    #获取一套试题及答案的html
    def get_a_html(self,cid,pid):
        # get请求 获得各种题型的答案
        html_questions = self.get_request(cid,pid)
        # post请求 获得各种题型的答案
        html_danxuan = self.post_request(cid,pid,'DANXUAN',html_questions)
        html_duoxuan = self.post_request(cid,pid,'DUOXUAN',html_danxuan)
        html_panduan = self.post_request(cid,pid,'PANDUAN',html_duoxuan)
        return html_panduan


    #获取4门科目*20 所有的试题及答案并存到本地文件中
    def get_html_all(self):
        for i in range(1,5):
            file_path = self.mk_dir(str(i))
            for j in range(1,21):
                html = self.get_a_html(i,j)
                self.write_file(file_path,str(j),'html',html.text)


    #创建文件夹的方法
    def mk_dir(self,folder_name):
        p = os.path.join(self.save_path, folder_name)
        if not os.path.exists(p):
            os.makedirs(p)
        else:
            print('%s文件夹已存在' % folder_name)
        return p


    #文件写入方法-覆盖
    def write_file(self,file_path,file_name,file_type,text):
        text_path = os.path.join(file_path, file_name + '.' + file_type)
        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(text)
    



    