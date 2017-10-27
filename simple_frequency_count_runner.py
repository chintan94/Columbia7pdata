#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:12:38 2017

Example script to display the usage of the Utils
@author: chintan94
"""
import file_read_util as fru
import frequency_count_util as fcu

fileReader = fru.FileReadUtil()
df = fileReader.read_tsv_into_data_frame('201601.tsv')

fc = fcu.FrequencyCountUtil()
freqDic = fc.freqCount(df)