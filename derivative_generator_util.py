#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 19:24:52 2017

@author: chintandoshi
"""

import pandas as pd

class DerivativeGeneratorUtil:
    
    ttm = {'kroger':['Kroger Co', 'KR'], 
           'chevron': ['Chevron Corporation', 'CVX'], 
           'wal - mart': ['Wal-Mart Stores Inc', 'WMT'], 
           'family dollar': ['Family Dollar Stores, Inc.', 'FDO'], 
           'mcdonald': ["McDonald's Corporation", 'MCD'], 
           'domino': ["Domino's Pizza Group", 'DOM'], 
           'sonic': ['Sonic Corporation', 'SONC'], 
           'fred': ["Fred's, Inc.", 'FRED'], 
           'shell service station': ['Royal Dutch Shell plc', 'RDS.A'], 
           'walgreens store': ['Walgreens Boots Alliance, Inc.', 'WBA'], 
           'wal wal - mart': ['Wal-Mart Stores Inc', 'WMT'], 
           'kroger fuel #': ['Kroger Co', 'KR']}
    
    tickers = [ ]
    def update_tickers(self,df):
        for i in range(len(df['transaction_description'])):
            if pd.isnull(df.loc[i,'ticker']):
                for j in self.ttm.keys():
                    if j in str(df.iloc[i,9]):
                        df.iloc[i,15] = self.ttm[j][1]
                        df.iloc[i,16] = self.ttm[j][0]
    
    def cleanup(self,df):
        df = df.dropna(subset=['accountholder_zip'])
        df = df.dropna(subset=['accountholder_birth_year'])
        df = df.dropna(subset=['accountholder_gender'])
    