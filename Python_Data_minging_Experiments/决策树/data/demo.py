#pandas 练习
import pandas as pd
data = pd.read_csv("lenses.data",sep = "  ",header=None)
print(data)
print("===")
print(data.ix[0:5])
data.ix[0:5].to_csv('data1.csv', header=None, index=False,mode='a')
data.ix[8:13].to_csv('data1.csv', header=None, index=False,mode='a')
data.ix[16:21].to_csv('data1.csv', header=None, index=False,mode='a')
data.ix[6:7].to_csv('data2.csv',header=None,index=False,mode='a')
data.ix[14:15].to_csv('data2.csv',header=None,index=False,mode='a')
data.ix[22:23].to_csv('data2.csv',header=None,index=False,mode='a')