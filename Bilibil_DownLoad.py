# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""



# coding: utf-8
import requests
import json
from lxml import etree
import os


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Referer': 'https://www.bilibili.com/video/BV1fx411M7Yx?p=1'
}

def GetBiliVideo(homeurl,num,session=requests.session()):
    res = session.get(url=homeurl, headers=headers)
    html = etree.HTML(res.content)  # homeurl的源代码

    videoinforms = str(html.xpath('//head/script[5]/text()')[0])[20:]
    videojson = json.loads(videoinforms)

    # 获取详情信息列表
    listinform = str(html.xpath('//head/script[6]/text()')[0]).replace('\u2022', '')[25:-122]
    listjson = json.loads(listinform)

    VideoURLs = []
    id = []
    for vj in videojson['data']['dash']['video']:
        if vj['id'] in id:
            continue
        else:
            id.append(vj['id'])
            VideoURLs.append(vj['baseUrl'])

    AudioURls = []
    id = []
    for vj in videojson['data']['dash']['audio']:
        if vj['id'] in id:
            continue
        else:
            id.append(vj['id'])
            AudioURls.append(vj['baseUrl'])

    # 获取文件夹的名称
    dirname = str(html.xpath("//h1/@title")[0])

    if not os.path.exists(dirname):
        os.makedirs(dirname)
        print('目录文件创建成功!')
    # 获取每一集的名称
    name=listjson['videoData']['pages'][num]['part']

    # 下载视频和音频
    print('正在下载 "'+name+'" 的视频····')
    for i, VideoURL in enumerate(VideoURLs):
        print(i)
        BiliBiliDownload(homeurl=homeurl,url=VideoURL, name=os.getcwd()+'/'+dirname+'/'+name + '_Video_{}.mp4'.format(i), session=session)
    print('正在下载 "' + name + '" 的音频····')
    for i, AudioURl in enumerate(AudioURls):
        print(i)
        BiliBiliDownload(homeurl=homeurl, url=AudioURl, name=os.getcwd() + '/' + dirname + '/' + name + '_Audio_{}.mp3'.format(i),
                         session=session)

def BiliBiliDownload(homeurl,url, name, session=requests.session()):
    headers.update({'Referer': homeurl})
    session.options(url=url, headers=headers,verify=False)
    # 下载数据
    begin = 0
    end = 1024*512-1
    flag=0
    while True:
        headers.update({'Range': 'bytes='+str(begin) + '-' + str(end)})
        res = session.get(url=url, headers=headers,verify=False)
        if res.status_code != 416:
            begin = end + 1
            end = end + 1024*512
        else:
            headers.update({'Range': str(end + 1) + '-'})
            res = session.get(url=url, headers=headers,verify=False)
            flag=1
        with open(name, 'ab') as fp:
            fp.write(res.content)
            fp.flush()
        if flag==1:
            fp.close()
            break

if __name__ == '__main__':
    # 下载视频
    GetBiliVideo('https://www.bilibili.com/video/BV1fx411M7Yx?p=1',0) # BV/Av
    exit(0)
    # 下载多个视频
    # url='https://www.bilibili.com/video/BV1wD4y1o7AS'
    # range_start = 2
    # range_end = 5
    # if int(range_start)<=int(range_end):
    #     for i in range(int(range_start),int(range_end)+1):
    #         print(i)
    #         GetBiliVideo(url+"?p="+str(i),i)
    # else:
    #     print('选集不合法！')


