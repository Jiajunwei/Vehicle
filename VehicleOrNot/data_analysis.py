#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/27 0027 上午 10:31
# @Author  : Lovin
# @Site    : 
# @File    : data_analysis.py
# @Software: PyCharm
import pandas as pd
import os

data_csv = pd.read_csv('rawData.csv')
model_frame = data_csv['modelID']
model_list = model_frame.tolist()
model_set = set(model_list)

image_frame = data_csv['imageName']

for model in model_set:
    # if model_list.count(model) > 500:
    print model,model_list.count(model)




