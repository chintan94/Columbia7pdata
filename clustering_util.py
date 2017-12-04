
# coding: utf-8

# In[1]:

import pandas as pd
import time
from collections import Counter
import file_read_util as fru
import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.cluster import Birch


from sklearn import preprocessing

class ClusterUtil:

    def processData(self,fileList):
        fileReader = fru.FileReadUtil()
        frame=[]
        nrows = []
        extension = '.tsv'
        
        #read data from csv
        for file in fileList:
            if file.endswith(extension):  
                print "Reading from " + file
                start = time.clock()
                df = fileReader.read_tsv_into_data_frame(file)
                [r,c] = df.shape
                nrows.append(r)
                frame.append(df)
                end = time.clock()
                print "Time taken for " + file + " " + str((end-start))
                print "appended " + str(r) + " rows"
        result = pd.concat(frame)
        
        # append month to the dataframe
        ind =[]
        for i in range(len(nrows)):
   
            for j in range(nrows[i]):
                ind.append(i)

        result['month'] = ind
        
        # process data feature: age and gender, turn them into numbers
        for i in range(len(result['accountholder_gender'])):
            if result.iat[i,6] != 0:
                result.iat[i,6] = 2017 - result.iat[i,6]
        
            if result.iat[i,7] == 'MALE':
                result.iat[i,7] = 1
            elif result.iat[i,7] == 'FEMALE':
                result.iat[i,7] = -1
            else:
                result.iat[i,7] = 0
                
        result['accountholder_gender'] = map(int,result['accountholder_gender'])
        
        #split dataframe by month and group subdataframe by person
        nd = []
        for i in range(len(nrows)):
            tempd = result.loc[result['month'] == i]
            account = tempd.groupby('accountholder_key')
            newdf = pd.DataFrame(dtype = float)
            newdf = account['transaction_amount_in_cents'].agg([np.size, np.sum])
            newdf['accountholder_zip'] = account['accountholder_zip'].agg([np.mean])
            newdf['accountholder_zip'] = map(round,newdf['accountholder_zip']/1000)
            newdf['accountholder_gender'] = account['accountholder_gender'].agg([np.mean])
            newdf['accountholder_age'] = account['accountholder_birth_year'].agg([np.mean])
            newdf['month'] = account['month'].agg([np.mean])
            nd.append(newdf)
        nd = pd.concat(nd)
        
        #clean data, drop null elements
        
        cleaned = nd.dropna(subset=['accountholder_zip'])
        cleaned = cleaned.dropna(subset=['accountholder_age'])
        cleaned = cleaned.dropna(subset=['accountholder_gender'])
        
        return cleaned
    
    
    def kmean(self,data,numofc):
        lable=[]
        for i in sorted(set(data['month'])):
            result1 = data.loc[data['month'] == i]
            result2 = result1.iloc[:,0:5]
            normdata = preprocessing.scale(result2)
            kmeans = KMeans(n_clusters=numofc).fit(normdata)
            lable.append(kmeans.labels_)
        lable= np.concatenate(lable)
        return lable
    
    def dbsca(self,data,ep,mins):
        lable=[]
        for i in sorted(set(data['month'])):
            result1 = data.loc[data['month'] == i]
            result2 = result1.iloc[:,0:5]
            normdata = preprocessing.scale(result2)
            dbscan = DBSCAN(eps=ep, min_samples=mins).fit(normdata)
            lable.append(dbscan.labels_)
        lable= np.concatenate(lable)
        return lable
    
    def birch(self,data,bf,th):
        lable=[]
        for i in sorted(set(data['month'])):
            result1 = data.loc[data['month'] == i]
            result2 = result1.iloc[:,0:5]
            normdata = preprocessing.scale(result2)
            brc = Birch(branching_factor=bf, threshold=th).fit(normdata)
            lable.append(brc.labels_)
        lable= np.concatenate(lable)
        return lable
        


# In[ ]:



