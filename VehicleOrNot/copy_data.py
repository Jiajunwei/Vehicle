#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 0025 下午 3:16
# @Author  : Lovin
# @Site    : 
# @File    : copy_data.py
# @Software: PyCharm
"""
按照csv名单将数据拷到一个文件夹中
"""
import pandas as pd
import shutil


#正负样本在同一文件夹

# src = r'D:/PreciseRecognition/Process/Raw_Data/images_train/images/'
#
# dst = r'./data/'
#
# data_csv = pd.read_csv('imageName_modelID_664.csv')
# imageName = data_csv['imageName']
#
#
# for i in imageName:
#     shutil.copy(src+i,dst)

#正负样本不在同一文件夹
# src1 = r'D:/PreciseRecognition/Process/Raw_Data/images_train/images/'
# src2 = 'D:/Data/negamples/negative/'
# dst = r'./data/'
#
# data_csv = pd.read_csv('imageName_modelID_664_2.csv')
# imageName_frame = data_csv['imageName']
#
#
# for imageName in imageName_frame:
#     if(imageName.split('.')[0][0] == '0'):
#         shutil.copy(src1 + imageName, dst)
#     else:
#         shutil.copy(src2 + imageName, dst)
#
#正负样本在同一文件夹下
src = 'D:/PreciseRecognition/Process/Raw_Data/images_train/images/'
dst = './verify/'

data_csv = pd.read_csv('image_100_to_verify.csv')
imageName_frame = data_csv['imageName']
modelID_frame = data_csv['modelID']

for imageName in imageName_frame:
    shutil.copy(src + imageName, dst)
# for i in range(len(data_csv)):
#     if modelID_frame[i] == 86 or modelID_frame[i] == 193:
        # print modelID_frame[i],imageName_frame[i]
        # print imageName_frame[i].split('.')[0] + '_' + str(modelID_frame[i]) + '.jpg'
        # shutil.copy(src + imageName_frame[i],dst)
        # with open('train86193.txt', 'a') as f1:
        #     f1.write("%s%s%d\n" % (imageName_frame[i], ' ', int(modelID_frame[i])))
        #
        # with open('test.txt', 'a') as f2:
        #     f2.write("%s%s%d\n" % (imageName_frame[i], ' ', int(modelID_frame[i])))



