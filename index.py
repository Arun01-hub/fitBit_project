from operator import le
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
df=pd.read_csv("D:\ML projects\heartrate_seconds_merged.csv")
#df = pd.read_csv('data.csv')
""" df=df.head(40)
df.plot(y="Value",x="Time")
plt.show()
print(df[["Value","Time"]]) """
""" c=0
id1=""
idlist=[]
for id in df["Id"]:
   if id!=id1:
       c=c+1 
       id1=id
       idlist.append(id) """
df1=df.loc[df["Id"]==2022484408]
# print(idlist[0])
""" print(df1.size)
df1.plot(x="Time",y="Value")
df2=df.loc[df["Id"]==idlist[1]]
print(df2.size)
df2.plot(x="Time",y="Value")
plt.show() """
# print(type(df1["Time"][1]))
l=len(df1["Time"])
X=[]
Y=[]
df=df1["Time"]
df2=df1["Value"]

for i in range(l):
    # print(str(df[i]))
    obj=re.search("^4/12/2016\s[1-12]:.*[AP]M$",str(df[i]))
    if obj:
        X.append(obj.group())
        Y.append(df2[i])
""" print(X)
print(Y) """
plt.plot(X,Y)
plt.show()

