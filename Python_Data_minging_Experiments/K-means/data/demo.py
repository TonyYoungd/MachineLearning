import pandas as pd

#数据转换
"""
#data1和data2的转换
data = pd.read_csv("data1.txt",sep="\t",header=None)
data.to_csv("data1.csv",index=None,header=None)
print(data)
"""



"""
#data.mat的转换
import scipy.io as sio
data1 = sio.loadmat("data.mat")
data = data1.get('X')
data2 = pd.DataFrame(data)
data2.to_csv("data.csv",index=None,header=None)
"""

"""
#bird.mat的转换
import scipy.io as sio
data1 = sio.loadmat("bird.mat")
data = data1.get('A')
for example in data:
    data = pd.DataFrame(example)
    data.to_csv("bird.csv",index=None,header=None,mode='a')
"""

