#切割数据集分为训练集和测试集
import pandas as pd

#读数据集
data = pd.read_csv("lenses.data",sep = "  ",header=None)
data.ix[0:5].to_csv('data_p.csv', header=None, index=False,mode='a')
data.ix[8:13].to_csv('data_p.csv', header=None, index=False,mode='a')
data.ix[16:21].to_csv('data_p.csv', header=None, index=False,mode='a')
data.ix[6:7].to_csv('data_t.csv',header=None,index=False,mode='a')
data.ix[14:15].to_csv('data_t.csv',header=None,index=False,mode='a')
data.ix[22:23].to_csv('data_t.csv',header=None,index=False,mode='a')






