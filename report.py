# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""
import re

import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool

house_datas = list()
price_data = list()
count_datas = 1
price_dict = {
    "100万以下" : 0,
    "100万到150万之间" : 0,
    "150万到200万之间" : 0,
    "200万到250万之间" : 0,
    "250万到300万之间" : 0,
    "300万到500万之间" : 0,
    "500万及以上" : 0,
    "价格面议" : 0,
}
size_dict = {
    "50平米以下" : 0,
    "50到100平米之间" : 0,
    "100到150平米之间" : 0,
    "150到200平米之间" : 0,
    "200到250平米之间" : 0,
    "250到300平米之间" : 0,
    "300平米及以上" : 0,
}

def get_data(html):
    global count_datas
    try:
        res = requests.get(html)
        res.encoding = "gbk"
    except:
        return ""
    soup = BeautifulSoup(res.text,"lxml") # 获取源代码
    data_list = soup.find_all("tr",attrs={"bgcolor":"#FFFFFF"})

    # 爬虫体
    for data in data_list:
        house_data = dict()
        house_data["序号"] = count_datas
        house_data["详细地址"] = data.find_all("a",attrs={"target":"_blank"})[0].string.strip()
        house_data["所在区域"] = data.find_all("td")[1].string
        house_data["详情链接"] = "http://www.lgfdcw.com/cs/"+data.find_all("a",attrs={"target":"_blank"})[0].attrs["href"]
        house_data["房型"] = data.find_all("td")[2].string
        house_data["户型"] = data.find_all("td")[3].string
        house_data["面积"] = data.find_all("td")[4].string[:-1] + "平方米"
        house_data["出售价格"] = data.find_all("td")[5].string.strip() if data.find_all("td")[5].string !=None else "面议"
        house_data["登记时间"] = data.find_all("td")[6].string.strip("[]")
        house_datas.append(house_data)
        count_datas += 1

        price = data.find_all("td")[5].string.strip() if data.find_all("td")[5].string != None else "面议"
        final_price = re.findall("\d+",price)[0]
        if final_price == "面议":
            price_dict["价格面议"] += 1
        elif "万" not in price:
            price_dict["价格面议"] += 1
        elif float(final_price) < 100:
            price_dict["100万以下"] += 1
        elif 100 <= float(final_price) < 150:
            price_dict["100万到150万之间"] += 1
        elif 150 <= float(final_price) < 200:
            price_dict["150万到200万之间"] += 1
        elif 200 <= float(final_price) < 250:
            price_dict["200万到250万之间"] += 1
        elif 250 <= float(final_price) < 300:
            price_dict["250万到300万之间"] += 1
        elif 300 <= float(final_price) < 500:
            price_dict["300万到500万之间"] += 1
        elif float(final_price) >= 500:
            price_dict["500万及以上"] += 1
        else:
            price_dict["价格面议"] += 1

        size = float(data.find_all("td")[4].string[:-1])
        if size < 50:
            size_dict["50平米以下"] += 1
        elif 50 <= size < 100:
            size_dict["50到100平米之间"] += 1
        elif 100 <= size < 150:
            size_dict["100到150平米之间"] += 1
        elif 150 <= size < 200:
            size_dict["150到200平米之间"] += 1
        elif 200 <= size < 250:
            size_dict["200到250平米之间"] += 1
        elif 250 <= size < 300:
            size_dict["250到300平米之间"] += 1
        else:
            size_dict["300平米及以上"] += 1

def sava_data(data_dict):
    # 写入excel
    final_data = pd.DataFrame(data_dict, columns = ["序号","详细地址","所在区域","详情链接","房型","户型","面积","出售价格","登记时间"])
    final_data.to_excel("house.xlsx", index=False)

    # 即将数据绘制
    plt.rcParams["font.family"] = "simhei"
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.unicode_minus'] = False

    plt.bar(list(price_dict.keys()), list(price_dict.values()) )
    plt.xticks(rotation = 90)
    plt.title("房价区间个数")
    for a,b in zip(list(price_dict.keys()), list(price_dict.values())):
        plt.text(a, b + 0.001, '%.f' % b, ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.show()

    plt.bar(list(size_dict.keys()), list(size_dict.values()))
    plt.xticks(rotation=90)
    plt.title("房屋面积区间个数")
    for a, b in zip(list(size_dict.keys()), list(size_dict.values())):
        plt.text(a, b + 0.001, '%.f' % b, ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.show()

    class_count = final_data["户型"].value_counts()
    plt.bar(list(class_count.keys()), list(class_count.values))
    plt.title("各户型个数")
    plt.xticks(rotation=90)
    plt.tight_layout()
    for a, b in zip(list(class_count.keys()), list(class_count.values)):
        plt.text(a, b + 0.001, '%.f' % b, ha='center', va='bottom', fontsize=9)
    plt.show()

    house_count = final_data["房型"].value_counts()
    plt.bar(list(house_count.keys()), list(house_count.values))
    plt.title("各房型个数")
    for a, b in zip(list(house_count.keys()), list(house_count.values)):
        plt.text(a, b + 0.001, '%.f' % b, ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    max_Thread = multiprocessing.cpu_count()
    pool = ThreadPool(max_Thread)
    pool.map(get_data, [f"https://www.lgfdcw.com/cs/index.php?&PageNo={i}" for i in range(1, 6)])
    pool.close()
    pool.join()
    sava_data(house_datas)