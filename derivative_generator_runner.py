#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 19:16:40 2017

@author: chintandoshi
"""

import os
import time
import file_read_util as fru
import derivative_generator_util as dgu

extension = '.tsv'
path_to_ttfd = '../dict_dump/ttfd'

dgUtil = dgu.DerivativeGeneratorUtil()
fileReader = fru.FileReadUtil()

file_list=[]
for root, dirs, files in os.walk("../txn"):
    for name in files:
        if(name.endswith(extension)):
            file_list.append(os.path.join(root, name))

for file in file_list:
    if file.endswith(extension):  
        print "Reading from " + file
        start = time.clock()
        df = fileReader.read_tsv_into_data_frame(file)
        dgUtil.update_tickers(df)
        df = df.dropna(subset=['ticker'])
        unique = df.ticker.unique()
        for i in unique:
            temp = df.loc[df.ticker==i]
            temp.to_csv(os.path.join(os.path.dirname(file),
                                     i + '.tsv'),
                                     sep = '\t',
                                     index = False,
                                     header = False)
        
        end = time.clock()
        print "Time taken for " + file + " " + str((end-start))
        break







