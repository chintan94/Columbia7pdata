#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:55:33 2017

Provides all the utilities related to the frequency counting
@author: chintan94, jihongtang
"""

import spacy
from collections import Counter


class FrequencyCountUtil:
    
    nlp = None
    string_format = 'utf8'
    
    def __init__(self):
       self.nlp = spacy.load('en')
       
    def process_desc(self,desc):
        return desc.rsplit(" ",2)[0].decode(self.string_format)
    
    def freqCount(self,df):
        frequency = Counter()
        desc_list = df['transaction_description']        
        for i in desc_list:
            if type(i) == str:
                doc = self.nlp(self.process_desc(i))
                for j in doc.ents:
                    frequency[j.lemma_] += 1
        return frequency