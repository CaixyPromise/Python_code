# -*- coding:utf-8 -*-

'''
CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

'''
# 天气爬虫
from bs4 import BeautifulSoup
from urllib.request import urlopen

def spider():
    # url = "http://www.weather.com.cn/"
    url = "http://www.weather.com.cn/weather/101010100.shtml"
    resp = urlopen(url)
    soup = BeautifulSoup(resp,"html.parser")
    target_Today = soup.find("p",class_ = "tem")
    try:
        temperatureHight = target_Today.span.string
    except AttributeError as e:
        temperatureHight = target_Today.find_next("p",class_="tem").span.string

    temperatureLow = target_Today.i.string
    weather = soup.find("p",class_ = "wea").string
    print(temperatureHight,temperatureLow,weather)


spider()

