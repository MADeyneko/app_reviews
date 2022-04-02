import codecs
import requests
import threading
from queue import Queue
import pandas as pd
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import progressbar
import math 
import os
import sys
from bs4 import BeautifulSoup
from lxml import html
import urllib
from datetime import datetime

class parse_html:

    def __init__(self) -> None:
        self.name=''
    
    def get_rewviews(self,name):
        self.name=name
        text=self.get_text_file()
        soup = BeautifulSoup(text)
        result=pd.DataFrame(columns = ['Кто','Оценка','Дата','Текст','Ответ'])
        all_reviews=soup.find_all('div', {'class': 'd15Mdf bAhLNe'})
        
        for review in all_reviews:
            who=review.find('span',{'class': 'X43Kjb'}).text
            star=review.find('div',{'class':'pf5lIe'}).contents[0]['aria-label'].replace('Средняя оценка: ','')
            date=review.find('span',{'class':'p2TkOb'}).text.replace(' г.', '')
            date=datetime(self.get_year(date), self.get_month(date), self.get_day(date))
            text=review.find('span',{'jsname':'fbQN7e'})
            if text == None :
                text =review.text 

            elif text.text == '':
                text=review.find('span',{'jsname':'bN97Pc'}).text               
            else:
                text=review.find('span',{'jsname':'fbQN7e'}).text

            ans=''


            result = pd.concat(
                    [result,
                    pd.DataFrame([
                        [who, star, date, text, ans]]
                        ,columns = ['Кто','Оценка','Дата','Текст','Ответ']
                        )
                    ]
                )
            
    

        return result
            # print(1)

    def get_year(self, d):
        d=d.split(' ')
        return int(d[2])

    def get_month(self, d):
        unit_to_multiplier = {
            'января': 1,
            'февраля': 2,
            'марта': 3,
            'апреля': 4,
            'мая': 5,
            'июня': 6,
            'июля': 7,
            'августа': 8,
            'сентября': 9,
            'октября': 10,
            'ноября': 11,
            'декабря': 12,
        }
        d=d.split(' ')
        
        return int(unit_to_multiplier[d[1]])

    def get_day(self, d):
        d=d.split(' ')
        return int(d[0])

    def get_text_file(self):
        # return open(self.name,'r').read()
        fileObj = codecs.open( self.name, "r", "utf_8_sig" )
        text = fileObj.read() # или читайте по строке
        fileObj.close()

        return text

if __name__=='__main__':
    res=pd.DataFrame()
    parse=parse_html()
    
    res=pd.concat(
        [
            res
            ,parse.get_rewviews('rev_1.html')
            ,parse.get_rewviews('rev_2.html')
            ,parse.get_rewviews('rev_3.html')
            ,parse.get_rewviews('rev_4.html')
            ,parse.get_rewviews('rev_5.html')
        ]
    )

    res.to_excel('test.xlsx', index=False)