#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 0024 下午 9:44
# @Author  : Lovin
# @Site    : 
# @File    : raw_data_process.py
# @Software: PyCharm
"""
取出所有model = 0的，和同等数量model！=0的
"""
import pandas as pd

src = r'D:/PreciseRecognition/Process/Raw_Data/images_train/images/'
dst = r'D:/PreciseRecognition/Process/Processed_Data/model_or_not/'

data_csv  = pd.read_csv('../DataProcess/rawData.csv')

data_model = data_csv['modelID']
data_imageName = data_csv['imageName']
model_list = data_model.tolist()
model_set = set(model_list)

new_model_list = []
new_imageName_list = []
count = 0
for i in range(len(data_csv)):
    if data_model[i] == 0:
        new_imageName_list.append(data_imageName[i])
        new_model_list.append(1)
    elif count < 664:
        new_imageName_list.append(data_imageName[i])
        new_model_list.append(0)
        count += 1
newDataFrame = pd.DataFrame({'imageName':new_imageName_list,'modelID':new_model_list})
newDataFrame.to_csv('imageName_modelID_664.csv',index=False)
