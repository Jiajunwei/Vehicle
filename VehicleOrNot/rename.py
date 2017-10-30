#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/27 0027 下午 3:00
# @Author  : Lovin
# @Site    : 
# @File    : rename.py
# @Software: PyCharm
import pandas as pd
import os

src = 'D:/PreciseRecognition/Process/Processed_Data/images_all/'


image_list = os.listdir(src)
data_csv = pd.read_csv('D:/PreciseRecognition/Process/Processed_Data/images_all_csv/images_all.csv')

modelID_frame = data_csv['model']
imageName_frame = data_csv['name']
modelID_list = modelID_frame.tolist()
modelID_set = set(modelID_frame)


for i in range(len(data_csv)):
    print imageName_frame[i],imageName_frame[i].split('.')[0]  + '_' + str(modelID_frame[i]) + '.jpg'
    if os.path.isfile(src + imageName_frame[i]) == True:
        os.rename(src + imageName_frame[i],src + imageName_frame[i].split('.')[0] + '_' + str(modelID_frame[i]) + '.jpg')

