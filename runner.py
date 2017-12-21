import pandas as pd
import os
import numpy as np
import clustering_util as clu

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
    newdf1 = pd.DataFrame(dtype = float)
    newdf2 = pd.DataFrame(dtype = float)
    for l in range(6,c):
        td1 = d1.groupby(header[l])
        td2 = d2.groupby(header[l])
        newdf1[header[l]] = td1['sum'].agg([np.sum])
        newdf2[header[l]] = td2['sum'].agg([np.sum])
    
    [nr,nc] = newdf1.shape
    
    for l1 in range(nr):
        for l2 in range(nc):
            newdf2.iat[l1,l2] = newdf2.iat[l1,l2]/newdf1.iat[l1,l2]-1
    
    return newdf2
        
    
def findBest(data, flag):
    [r,c] = data.shape
    header = data.columns.values
    cluster = []
    if flag == 1:
        for i in range(c):
            col = header[i]
            cl = data[col].idxmax()
            cluster.append(cl)
        result = max(cluster)
        name = header[cluster.index(max(cluster))]
        
    if flag == -1:
        for i in range(c):
            col = header[i]
            cl = data[col].idxmin()
            cluster.append(cl)
        result = min(cluster)
        name = header[cluster.index(min(cluster))]
    return name, result

#main function:
fl=[]
for root, dirs, files in os.walk("../test/"):
    for name in files:
        fl.append(os.path.join(root, name))


proData = clu.ClusterUtil()
data = proData.processData(fl)

data_kmeans = runCluster(data,'kmeans',3,5,3)
data_db = runCluster(data,'dbscan',0.3,1.2,3,3,5,3)
#data_bir = runCluster(data,'birch',25,70,3,0.1,1,3)
da1 = findSimilar(data_kmeans,10,11)
da2 = findSimilar(data_db,10,11)
#da3 = findSimilar(data_bir,10,11)

[name1, result1] = findBest(da1,1)
[name2, result2] = findBest(da2,1)
#[name3, result3] = findBest(da3,1)
