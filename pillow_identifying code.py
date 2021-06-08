# -*- coding:utf-8 -*-

'''
CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

'''

import random
import string
from PIL import Image, ImageFont, ImageDraw

stri = string.ascii_letters + string.digits # creat indentify code
bg = (255,255,255)
width_height = (250,100)
str_num = 8

def get_select_len(lenth):
    content = ""
    for i in range(lenth):
        content += random.choice(stri)
    print(content)
    return content

def get_color():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    return (R,G,B)


def main_photo(size,str_num,bg):

    imageTemp = Image.new("RGB",size,bg)
    font = ImageFont.truetype("font\Font_1.ttf",48)
    draw = ImageDraw.Draw(imageTemp)
    text = get_select_len(str_num)
    width, height = draw.textsize(text, font)

    offset = 2
    for i in range(str_num):
        offset += width//str_num
        position = (offset,(size[1]-height)//2+random.randint(-10,10))
        draw.text(xy = position,text = text[i],font=font,fill =get_color())

    imageFinal = Image.new("RGB",size,bg)
    pixelsFinal = imageFinal.load()
    pixelTemp = imageTemp.load()

    for y in range(0,size[1]):
        offset = random.randint(-1,1)
        for x in range(0,size[0]):
            newx = x+offset
            if newx >= size[0]:
                newx = size[0] - 1
            elif newx < 0:
                newx = 0
            pixelsFinal[newx,y] = pixelTemp[x,y]
    draw = ImageDraw.Draw(imageFinal)

    for i in range(int(size[0]*size[1]*0.07)):
        draw.point((random.randint(0,size[0]),random.randint(0,size[1])),fill=get_color())

    for i in range(8):
        start = (0,random.randint(0,size[1]-1))
        end = (size[0],random.randint(0,size[1]-1))
        draw.line([start,end],fill=get_color(),width = 1)

    for i in range(8):
        start = (-50,-50)
        end = (size[0]+10, random.randint(0,size[1]+10))
        draw.arc(start+end,0,360,fill=get_color())

    imageFinal.save("identify_CODE.jpg")
    imageFinal.show()


if __name__ == '__main__':
    main_photo(width_height,str_num,bg)


