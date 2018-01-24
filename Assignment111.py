# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:49:12 2018

@author: Prathyusha Mallela
"""

import pandas as pd
import numpy as np
#the_result=pd.Series([1, 2, 0, 1, 2, 3, 4, 0, 1, 2]);
df=pd.DataFrame({'X':[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]});
dfList=df['X'].tolist()
dist=0
fin_list=[]
for x in dfList:
    if dfList.index(x)==0:
     #print(x)
     j=1
     dist=j
     #print(dist)
    elif x==0:
     #print(x)
     j=0
     dist=j
     #print(dist)
    elif x!=0:
     #print(x)
     j=j+1
     dist=j
     #print(dist)
    fin_list.append(dist)

#print(fin_list)
#df=df.append({'Y':fin_list},ignore_index=False)
#df1=pd.Series(fin_list)
#print(df1)
df2=pd.DataFrame(fin_list,columns=['Y'])
#print(df2)
concat=pd.concat([df,df2],axis=1)
print(concat)