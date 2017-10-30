#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 0025 上午 11:03
# @Author  : Lovin
# @Site    : 
# @File    : select_some_to_csv.py
# @Software: PyCharm
"""
每类选取m个到训练列表train.csv，n个到测试列表test.csv
"""
import pandas as pd

# data_csv = pd.read_csv('imageName_modelID_664_2.csv')
data_csv = pd.read_csv('rawData.csv')
data_imageName = data_csv['imageName']
data_modelID = data_csv['modelID']
modelID_list = data_modelID.tolist()

# modelID_set = set(modelID_list)
modelID_set = set([86,193])


new_imageName_train_list = []
new_modelID_train_list = []
new_imageName_test_list = []
new_modelID_test_list = []
new_imageName_verify_list = []
new_modelID_verify_list = []

#对于modelID_set中的modelID，每个取出4000个训练，1000个测试
for modelID in modelID_set:
    count = 0
    for i in range(len(data_csv)):
        if data_modelID[i] == modelID:
            if count < 400:
                # new_imageName_train_list.append(data_imageName[i].split('.')[0]  + '_' + str(data_modelID[i]) + '.jpg')
                new_imageName_train_list.append(data_imageName[i])
                new_modelID_train_list.append(data_modelID[i])
            elif count < 500:
                # new_imageName_test_list.append(data_imageName[i].split('.')[0]  + '_' + str(data_modelID[i]) + '.jpg')
                new_imageName_test_list.append(data_imageName[i])
                new_modelID_test_list.append(data_modelID[i])
            elif count < 600:
                # new_imageName_verify_list.append(data_imageName[i].split('.')[0]  + '_' + str(data_modelID[i]) + '.jpg')
                new_imageName_verify_list.append(data_imageName[i])
                new_modelID_verify_list.append(data_modelID[i])
            else:
                pass
            count += 1

newDataFrame_train = pd.DataFrame()
newDataFrame_train['imageName'] = new_imageName_train_list
newDataFrame_train['modelID'] = new_modelID_train_list
newDataFrame_train.to_csv('image_400_to_train.csv',index=False)

newDataFrame_test = pd.DataFrame({'imageName':new_imageName_test_list,'modelID':new_modelID_test_list})
newDataFrame_test.to_csv('image_100_to_test.csv',index=False)

newDataFrame_verify = pd.DataFrame()
newDataFrame_verify['imageName'] = new_imageName_verify_list
newDataFrame_verify['modelID'] = new_modelID_verify_list
newDataFrame_verify.to_csv('image_100_to_verify.csv',index=False)