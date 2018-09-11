"""
    按时间切割数据，每个小时为一个时间段
    保存在“../data_new/”中
       
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
from pandas.tseries.offsets import *
#加载目录下的所有文件
loc = "../../data/Taxi_070220/"
loc_new = "../data_new/"
dirs = os.listdir("../../data/Taxi_070220")
hour = Hour()
data_time = []
#时间序列
start = pd.to_datetime("2007-02-20 00:00:00")
for k in range(len(dirs)):
    end = hour.apply(start)
    # 遍历每个文件
    for i in dirs:
        dataSet = pd.read_csv(loc+i, header=None)
        #将第一列转化为时间
        dataSet[1] = dataSet[1].astype('datetime64[ns]')
        #提取出时间段内的数据
        data = dataSet.loc[(dataSet[1] >= start) & (dataSet[1] <= end)]
        data.to_csv(loc_new+str(start), header=None, mode='a')
        continue
    start = end
