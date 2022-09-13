import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("D:\ML projects\heartrate_seconds_merged.csv")
df=df.head(50000)
df[["Date","Time","Noon"]]=df["Time"].str.split(' ',2,expand=True)
df[["hh","mm","ss"]]=df["Time"].str.split(':',2,expand=True)
df[["mn","dt","yyyy"]]=df["Date"].str.split('/',2,expand=True)
def find_hr_avg(date,month,year,hour,noon):
    dfo=df.loc[ (df["Noon"]==noon) & (df["dt"]==date) & (df["mn"]==month) & (df["hh"]==str(hour)) & (df["yyyy"]==year)]
    hr_avg=None
    if len(dfo["Value"])!=0:
        hr_avg=(sum(dfo["Value"])/len(dfo["Value"]))
    return hr_avg
X=[]
Y=[]
# print(df["hh"].drop_duplicates(keep='first'))
# print(df["yyyy"].drop_duplicates(keep='first'))
for y in df["yyyy"].drop_duplicates(keep='first'):
    for m in df["mn"].drop_duplicates(keep='first'):
        for d in df["dt"].drop_duplicates(keep='first'):
            X.append([])
            Y.append([])
            for n in df["Noon"].drop_duplicates(keep='first'):
                for h in sorted(pd.to_numeric((df["hh"].drop_duplicates(keep='first')))):
                    val=find_hr_avg(d,m,y,h,n)
                    if val != None:
                        if n=="AM":
                            if h=="12":
                               X[len(X)-1].append(0)
                            else:
                               X[len(X)-1].append(int(h)) 
                        else:
                            if h=="12":
                                X[len(X)-1].append(int(h))
                            else:
                               X[len(X)-1].append(int(h)+12)
                        Y[len(Y)-1].append(val)
                        
# print(sorted(pd.to_numeric((df["hh"].drop_duplicates(keep='first')))))
# print(X,Y)
# print("enter date value:")
# i=int(input())
# print("enter noon value")
# j=int(input())
plt.subplot(3,3,1)
plt.plot(X[1],Y[1])
plt.subplot(3,3,2)
plt.plot(X[2],Y[2])
plt.subplot(3,3,3)
plt.plot(X[3],Y[3])
plt.subplot(3,3,4)
plt.plot(X[4],Y[4])
plt.subplot(3,3,5)
plt.plot(X[5],Y[5])
plt.subplot(3,3,6)
plt.plot(X[6],Y[6])
plt.subplot(3,3,7)
plt.plot(X[7],Y[7])
plt.show()
""" df.plot(x="mm",y="Value")
plt.show() """

    