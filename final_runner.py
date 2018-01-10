
# coding: utf-8

# In[1]:


import pandas as pd
import time
from collections import Counter
import file_read_util as fru
import os
import numpy as np
import matplotlib.pyplot as plt
import clustering_util as clu
from os.path import join, getsize

# name = ['kmeans','dbscan','birch'], for dbscan [eps, min_samples], for birch[branching_factor,threshold]
# cluster for kmeans must be integer, min_samples for dbscan and branching factor for birch must be integer as well
def runCluster(data, name,l1,u1,s1,l2=0,u2=0,s2=0):
    
    if name == 'kmeans':
        noc = np.linspace(l1,u1,num=s1)
        for i in noc:
            inti = int(i)
            header = name + ',' + str(inti)
            
            lable = proData.kmean(data,inti)
            data[header] = lable
    elif name == 'dbscan':
        noc1 = np.linspace(l1,u1,num=s1)
        noc2 = np.linspace(l2,u2,num=s2)
        for i1 in noc1:
            for i2 in noc2:
                inti2 = int(i2)
                header = name + ',' + str(i1) + ',' + str(inti2)
                
                lable = proData.dbsca(data,i1,inti2)
                data[header] = lable
    elif name == 'birch':
        noc1 = np.linspace(l1,u1,num=s1)
        noc2 = np.linspace(l2,u2,num=s2)
        for i1 in noc1:
            for i2 in noc2:
                inti1 = int(i1)
                header = name + ',' + str(inti1) + ',' + str(i2) 
              
                lable = proData.birch(data,inti1,i2)
                data[header] = lable
                
    else:
        print 'Error : no such clustering algorithm'
    
    return data


def findSimilar(data, prem, nexm):
    header = data.columns.values
    [r,c]= data.shape
    d1 = data.loc[data['month'] == prem]
    d2 = data.loc[data['month'] == nexm]
    #find similar cluster in next month
    for i in range(6,c):
        macount = []
        for j in sorted(set(d1.iloc[:,i])):
            temp = d1.loc[d1[header[i]] == j]
            count_lable = []
            for j1 in sorted(set(d2.iloc[:,i])):
                count = 0
                temp1 = d2.loc[d2[header[i]] == j1]
                for k in temp1.index:
                    
                    if k in temp.index:
                        count = count+1
                count_lable.append(count)
            macount.append(count_lable.index(max(count_lable)))
        #print macount
        for q in range(len(d2.iloc[:,i])):
            if d2.iat[q,i] in macount:
                d2.iat[q,i] = macount.index(d2.iat[q,i])
            else:
                d2.iat[q,i] = -1
    #print d1
    #compute the growth of total spending
    spending=[]
    newdf1 = pd.DataFrame(dtype = float)
    newdf2 = pd.DataFrame(dtype = float)
    head = []
    ps=[]
    nx=[]
    for l in range(6,c):
        head.append([header[l]])
        td1 = d1.groupby(header[l])
        td2 = d2.groupby(header[l])
        ps.append(td1['sum'].agg([np.mean]))
        nx.append( td2['sum'].agg([np.mean]))
    #print head
    #print nx
    res=[]
    for i in range(len(head)):
        a1 = ps[i]
        a2 = nx[i]
        for j in range(len(a2['mean'])):
            ind = a2.index[j]
            if ind in a1.index:
                if ind > -1:
                    a2.iat[j,0] = a2.iat[j,0]/a1.loc[ind]-1
                else:
                    a2.iat[j,0] = 0
            else:
                a2.iat[j,0]=0
                
        res.append(a2)
    #nheader = newdf1.columns.values
    #[nr,nc] = newdf1.shape
    
    #for l1 in range(nr):
        #for l2 in range(nc):
            #newdf2.iat[l1,l2] = newdf2.iat[l1,l2]/newdf1.iat[l1,l2]-1
    
    return res
        
    



def findBest(data,flag):
    cluster=[]
    value=[]
    if flag == 1:
        for i in range(len(data)):
            d = data[i]
            value.append(d['mean'].max()) 
            cluster.append(d['mean'].idxmax())
        ind = value.index(max(value))
        
    
    elif flag == -1:
        for i in range(len(data)):
            d = data[i]
            value.append(d['mean'].min()) 
            cluster.append(d['mean'].idxmin())
        ind = value.index(min(value))
        
    return data[ind].index.name, cluster[ind]
            
            
            
#main function:
fl=[]
for root, dirs, files in os.walk("."):
    for name in files:
        fl.append(os.path.join(root, name))


proData = clu.ClusterUtil()
data = proData.processData(fl)

data_kmeans = runCluster(data,'kmeans',3,5,3)
data_db = runCluster(data,'dbscan',0.3,1.2,3,3,5,3)
#data_bir = runCluster(data,'birch',25,70,3,0.1,1,3)
da1 = findSimilar(data_kmeans,8,9)
da2 = findSimilar(data_db,8,9)
#da3 = findSimilar(data_bir,10,11)


[name1, result1] = findBest(da2,1)
#[name2, result2] = findBest(da2,1)
#[name3, result3] = findBest(da3,1)


# In[2]:


print name1


# In[3]:


df_t1 = data_db.loc[data_db['month'] == 8]
df_t2 = df_t1.loc[df_t1[name1] == result1]
akey = df_t2.index # akey is all the user id in the best cluster of the best cluster methods


# In[4]:


clu=[] #constains three values, the cluster in Oct, Nov, and Dec that is most similar to the best cluster in Sep
for i in range(9,12):
    df3 = data_db.loc[data_db['month'] == i]
    c=[]
    for j in range(len(df3.index)):
        if df3.index[j] in akey:
            c.append(df3[name1].iat[j])
    clu.append(max(set(c), key=c.count))


# In[5]:


average_spend=[] #this gives you the final result, average spending of a person in the best cluster in Oct, Nov, Dec
for i in range(9,12):
    df4 = data_db.loc[data_db['month'] == i]
    df5  = df4.groupby(name1)
    df6 = df5['sum'].agg(np.mean)
    average_spend.append(df6.loc[clu[i-9]])


# In[6]:


average_spend


# In[7]:


data_db


# In[8]:


da2


# In[10]:


name1


# In[11]:


result1


# In[12]:


clu

