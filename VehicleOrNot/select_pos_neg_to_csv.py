#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 0026 上午 9:28
# @Author  : Lovin
# @Site    : 
# @File    : select_pos_neg_to_csv.py
# @Software: PyCharm
"""
从正负样本文件夹中各随机选取一定数量的正负样本
"""
import pandas as pd
import random
import os

new_imageName_list = []
new_modelID_list = []
pos_label_list = []
neg_label_list = []
#选取正样本
pos_list = os.listdir('D:/PreciseRecognition/Process/Raw_Data/images_train/images')
pos_random_list = random.sample(pos_list,664)
for _ in range(len(pos_random_list)):
    pos_label_list.append(0)
#选取负样本
neg_list = os.listdir('D:/Data/negamples/negative')
neg_random_list = random.sample(neg_list,664)
for _ in range(len(neg_random_list)):
    neg_label_list.append(1)

new_imageName_list = pos_random_list + neg_random_list
new_modelID_list = pos_label_list + neg_label_list

newDataFrame = pd.DataFrame({'imageName':new_imageName_list,'modelID':new_modelID_list})
newDataFrame.to_csv('imageName_modelID_664_2.csv',index=False)