#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:12:38 2017

@author: chintandoshi
"""
import file_read_util as fru
import frequency_count_util as fcu

fileReader = fru.FileReadUtil()
df = fileReader.read_tsv_into_data_frame('201601.tsv', rows = 10000)

fc = fcu.FrequencyCountUtil()
freqDic = fc.freqCount(df)

print freqDic