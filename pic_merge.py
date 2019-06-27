#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:15:18 2019

@author: meiyiteng
"""

import os
import math
import random
from PIL import Image

pic_dir='/Users/meiyiteng/Downloads/毕业照片'
source_dir=pic_dir+'/source_dir'
trans_dir=pic_dir+'/trans_dir'
result_dir=pic_dir+'/result_dir'

HEIGHT_PER_PIC=1000
WIDTH_PER_PIC = 1000

def getImagesName(Dir):
    allPicPath = []  # 所有图片
    for root, dirs, files in os.walk(Dir):
        for file in files:
            # 可自行添加图片的类型判断
            if file.endswith('.jpeg') or file.endswith('.JPG') or file.endswith('.jpg'):
                allPicPath.append(Dir +'/'+ file)
    return allPicPath

def transferSize(allPicPath):
    for i in range(len(allPicPath)):
        # 打开图片
        im = Image.open(allPicPath[i])
        # 重新设置图片的大小
        out = im.resize((HEIGHT_PER_PIC, WIDTH_PER_PIC),Image.NEAREST)
        # 将图片保存到固定的位置
        out.save(trans_dir + '/' + str(i) + '.jpeg')
        
def produce_wordpic(words):
    # 根据目录获取所有图片的路径
    allPicPath = getImagesName(source_dir)
    print(allPicPath)
    # 将所有图片转化成统一的大小（长宽均设定为100）
    transferSize(allPicPath)

    # 获取所有转换大小后的图片的路径
    allTransPicPath = getImagesName(trans_dir)

    # 打印路径，检查是否正确
    # print(allTransPicPath)

    # 得到用于拼图的图片的数量
    #numOfPic = sum([sum(eval(word)) for word in words])
    #print(numOfPic)
    # 因为设计拼接后的图形为正方形，因而对图片数量开算数平方根后向下取整，得到拼接后的正方形每行需要的小图片的数量
    #perPicNum = max([len(eval(i)) for i in words])

    # 生成一个固定的大小的image，类似于画布的感觉，用于将所有的图片贴上去，再生成新的图片
    #toImage = Image.new('RGBA', (perPicNum * HEIGHT_PER_PIC, perPicNum * WIDTH_PER_PIC))

    # 随机打乱转化大小后的图片的顺序，防止图片多余的情况下每次在后头的图片都无法用于拼接，也可使每次拼接出的图顺序不一样
    #random.shuffle(allTransPicPath)

    # 遍历用于拼接的图片，将每张图片拼接到指定位置
    j=0
    for word in words:
                 
        # 计算每个图片的位置，保证顺利拼接
        perPicNum=len(eval(word))
        toImage = Image.new('RGBA', (perPicNum * HEIGHT_PER_PIC, perPicNum * WIDTH_PER_PIC))
        for pos in loc_pos(eval(word)):
            fromImage = Image.open(allTransPicPath[j])
            j+=1
            wide,high=pos
            loc = (high * HEIGHT_PER_PIC, wide * WIDTH_PER_PIC)
            # 打印每个图片所在的位置，可以看出分布
            #print(loc)
            # 在上述生成的画布image上粘贴图片到指定位置
            toImage.paste(fromImage, loc)
    # 在画布上粘贴所有图片后将画布保存到指定位置
        toImage.save(result_dir + '/'+word+'.png')


x=[[1,0,0,0,1],
   [0,1,0,1,0],
   [0,0,1,0,0],
   [0,1,0,1,0],
   [1,0,0,0,1]]

m=[[1,0,0,0,1],
   [1,1,0,1,1],
   [1,0,1,0,1],
   [1,0,0,0,1],
   [1,0,0,0,1]]

u=[[1,0,0,0,1],
   [1,0,0,0,1],
   [1,0,0,0,1],
   [1,0,0,0,1],
   [1,1,1,1,1]]

words=['x','m','u']


def loc_pos(word):
    word=np.array(word)
    why,myt=np.where(word==1)
    pos=[i for i in zip(why,myt)]
    return pos




if __name__ == '__main__':
    produce_wordpic(words)
