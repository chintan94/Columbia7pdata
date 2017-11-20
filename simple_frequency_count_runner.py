#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:12:38 2017

Example script to display the usage of the Utils
@author: chintan94
"""
import os
import file_read_util as fru
import frequency_count_util as fcu

fileReader = fru.FileReadUtil()
file_list=[]
for root, dirs, files in os.walk("../txn"):
    for name in files:
        if(name.endswith('.tsv')):
            file_list.append(os.path.join(root, name))

df = fileReader.read_tsv_into_data_frame(file_list[0], rows = 100000)

fc = fcu.FrequencyCountUtil()
freqDic = fc.freqCount(df)