#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:55:33 2017
This class provides all the utilities related to the frequency counting
@author: chintandoshi, jihongtang
"""

import spacy
from collections import Counter


class FrequencyCountUtil:
    
    nlp = None
    string_format = 'utf8'
    
    def __init__(self):
       self.nlp = spacy.load('en')
       
    def token_without_last2(a):
        b=[]
        for i in a:
            sample = i.split()
            nsam = sample[0:-2]
            nstring = ' '.join(nsam)
            b.append(nstring)
        return b
    
    def process_desc(self,desc):
        return desc.rsplit(" ",2)[0].decode(self.string_format)
    
    def freqCount(self,df):
        frequency = Counter()
        desc_list = df.iloc[:,9]
        
        for i in desc_list:
            doc = self.nlp(self.process_desc(i))
            for j in doc.ents:
                frequency[j.lemma_] += 1
        return frequency