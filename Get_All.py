# coding:utf-8

from Get_Html import Get_Html
from Get_Questions import Get_Questions

class Get_All:
    def __init__(self):
        self.subject_set_1=set([])
        self.subject_set_2=set([])
        self.subject_set_3=set([])
        self.subject_set_4=set([])

    def get_all_subject(self):
        for cid in range(1,2):
            subject = []
            for pid in range(1,3):
                html = Get_Html().get_a_html(cid,pid)
                subject = subject + Get_Questions(html).parse_html()

            if cid == 1:
                print("cid=1: size = %s" % len(subject))
                self.subject_set_1.update(subject)
            elif cid == 2:
                print("cid=2: size = %s" % len(subject))
                self.subject_set_2.update(subject)
            elif cid == 3:
                print("cid=3: size = %s" % len(subject))
                self.subject_set_3.update(subject)
            elif cid == 4:
                print("cid=4: size = %s" % len(subject))
                self.subject_set_4.update(subject)

        print(self.subject_set_1)
        print(self.subject_set_2)
        print(self.subject_set_3)
        print(self.subject_set_4)


Get_All().get_all_subject()




