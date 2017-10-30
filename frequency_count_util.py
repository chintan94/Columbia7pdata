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
        return desc.rsplit(" ",2)[0].decode(self.string_format).title()
    
    def freqCount(self,df):
        frequency = Counter()
        for index, row in df.iterrows():
            if type(row['transaction_description']) == str:
                if type(row['ticker']) != str:
                    doc = self.nlp(self.process_desc(row['transaction_description']))
                    for j in doc.ents:
                        if j.lemma_.isdigit() is False:
                            frequency[j.lemma_] += 1
        return frequency

                    
                    