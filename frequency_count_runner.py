#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:30:14 2017

@author: chintandoshi
"""

import os
import time
from collections import Counter
import file_read_util as fru
import frequency_count_util as fcu

fileReader = fru.FileReadUtil()
path_to_tsvs = '.'
extension = '.tsv'
fc = fcu.FrequencyCountUtil()
fc = fcu.FrequencyCountUtil()

result_freq_dic = Counter()

file_list = os.listdir(path_to_tsvs)
for file in file_list:
    if file.endswith(extension):  
        print "Reading from " + file
        start = time.clock()
        df = fileReader.read_tsv_into_data_frame(file)
        freq_dic = fc.freqCount(df)
        result_freq_dic += freq_dic
        end = time.clock()
        print "Time taken for " + file + " " + str((end-start))
print result_freq_dic 
dict((k,result_freq_dic[k]) for k in result_freq_dic.keys() if result_freq_dic[k] > 200)   




        

        