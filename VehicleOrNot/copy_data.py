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

src = 'D:/PreciseRecognition/Process/Raw_Data/images_train/images/'
dst = './verify/'

data_csv = pd.read_csv('image_100_to_verify.csv')
imageName_frame = data_csv['imageName']
modelID_frame = data_csv['modelID']

for imageName in imageName_frame:
    shutil.copy(src + imageName, dst)



