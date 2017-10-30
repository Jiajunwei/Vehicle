#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 0025 下午 2:55
# @Author  : Lovin
# @Site    : 
# @File    : csv_to_txt.py
# @Software: PyCharm
"""
将csv中的数据转存到txt文件中
"""
import pandas as pd

data_csv1 = pd.read_csv('image_400_to_train.csv')
data_csv2 = pd.read_csv('image_100_to_test.csv')

with open('train.txt', 'w') as f1:
    for i in range(len(data_csv1)):
        f1.write("%s%s%d\n"%(data_csv1['imageName'][i],' ',int(data_csv1['modelID'][i])))

with open('test.txt', 'w') as f2:
    for i in range(len(data_csv2)):
        f2.write("%s%s%d\n"%(data_csv2['imageName'][i],' ',int(data_csv2['modelID'][i])))

