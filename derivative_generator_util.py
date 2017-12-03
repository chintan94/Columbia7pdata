#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 19:24:52 2017

@author: chintandoshi
"""

import pandas as pd

class DerivativeGeneratorUtil:
    
    ttm = {'wal-mart': ['Wal-Mart Stores Inc', 'WMT'], 
           'kroger':['Kroger Co', 'KR'], 
           'chevron': ['Chevron Corporation', 'CVX'], 
           'family dollar': ['Family Dollar Stores, Inc.', 'FDO'], 
           'mcdonald': ["McDonald's Corporation", 'MCD'], 
           'domino': ["Domino's Pizza Group", 'DOM'], 
           'sonic': ['Sonic Corporation', 'SONC'], 
           'freds': ["Fred's, Inc.", 'FRED'], 
           'shell service station': ['Royal Dutch Shell plc', 'RDS.A'], 
           'walgreens store': ['Walgreens Boots Alliance, Inc.', 'WBA'],
           'barnes&noble.com-bn': ['Barnes & Noble, Inc.','BKS'],
           'wm supercenter':['Wal-Mart Stores Inc', 'WMT'],
           'microsoft':['Microsoft Corporation','MSFT'],
           'google':['Alphabet Inc','GOOG'],
           'netflix':['Netflix, Inc','NFLX'],
           'amazon':['Amazon.com, Inc','AMZN'],
           'target':['Target Corporation','TGT'],
           'wendy':["The Wendy's Company",'WEN'],
           'cvs':['CVS Health Corporation','CVS'],
           'exxonmobil':['Exxon Mobil Corporation','XOM']
           }
    
    tickers = [ ]
    def update_tickers(self,df):
        for i in range(len(df['transaction_description'])):
            if pd.isnull(df.loc[i,'ticker']):
                temp = str(df.iat[i,9]).lower()
                for j in self.ttm.keys():
                    if j in temp:
                        df.iat[i,16] = self.ttm[j][1]
                        df.iat[i,17] = self.ttm[j][0]
                        break
                    
    def cleanup(self,df):
        df = df.dropna(subset=['accountholder_zip'])
        df = df.dropna(subset=['accountholder_birth_year'])
        df = df.dropna(subset=['accountholder_gender'])
    