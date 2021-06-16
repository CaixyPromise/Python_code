# -*- coding:utf-8 -*-

'''
CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

'''
import requests
import time
import re
from PIL import Image


def ptqrToken(qrsig):
    # 计算ptqrtoken
    e = 0
    for c in qrsig:
        e += (e << 5) + ord(c)
    return e & 0x7fffffff


def QR():
    # 获取 二手东 QQ扫码 二维码图片
    url = 'https://ssl.ptlogin2.qq.com/ptqrshow?appid=716027609&e=2&l=M&s=3&d=72&v=4&t=0.28351309688526216&daid=383&pt_3rd_aid=0'

    try:
        r = requests.get(url)
        qrsig = requests.utils.dict_from_cookiejar(r.cookies).get('qrsig')
        with open(r'QQ.png', 'wb') as f:
            f.write(r.content)
        im = Image.open(r'QQ.png')
        im = im.resize((350, 350))
        im.show()
        print(time.strftime('%H:%M:%S'), '登录二维码获取成功')
        return qrsig
    except Exception as e:
        print(e)


def Get_QQ():
    qrsig = QR()
    ptqrtoken = ptqrToken(qrsig)
    while True:
        url = 'https://ssl.ptlogin2.qq.com/ptqrlogin?u1=https%3A%2F%2Fgraph.qq.com%2Foauth2.0%2Flogin_jump&ptqrtoken=' + str(
            ptqrtoken) + '&ptredirect=0&h=1&t=1&g=1&from_ui=1&ptlang=2052&action=0-0-' + str(int(
            time.time() * 1000)) + '&js_ver=21050810&js_type=1&login_sig=&pt_uistyle=40&aid=716027609&daid=383&pt_3rd_aid=100273020&has_onekey=1&'
        cookies = {'qrsig': qrsig}
        try:
            r = requests.get(url, cookies=cookies)
            if '二维码未失效' in r.text:
                print(time.strftime('%H:%M:%S'), '二维码未失效')
            elif '二维码认证中' in r.text:
                print(time.strftime('%H:%M:%S'), '二维码认证中')
            elif '二维码已失效' in r.text:
                print(time.strftime('%H:%M:%S'), '二维码已失效')
                qrsig = QR()
                ptqrtoken = ptqrToken(qrsig)
            else:
                print(time.strftime('%H:%M:%S'), '登录成功')
                qq_number = re.findall(r'&uin=(.+?)&service', r.text)[0]
                return qq_number
        except Exception as e:
            print(e)
        time.sleep(2)


if __name__ == '__main__':
    print(Get_QQ())
