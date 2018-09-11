#--构建坐标数据列表---
import pandas as pd
import os
import csv
import matplotlib.pyplot as plt
file = pd.read_csv('../data/data_updown/pick.csv',header=None)
df = file.values
upjing = []
upwei = []
tenMinute = []
#-------构建各个经纬度数据列表---------
for i in range(0,24):
    upjing.append([])
    upwei.append([])
for i in range(0,len(df)):
    j = int(df[i][1][11])*10+int(df[i][1][12])
    upjing[j].append(df[i][2])
    upwei[j].append(df[i][3])
#坐标写进sample文件

for time, m in enumerate(upjing):
    sample = []
    for n, jing in enumerate(m):
        data = []
        data.append(jing)
        data.append(upwei[time][n])
        print(data)
        sample.append(data)
    dataSet = pd.DataFrame(sample)
    dataSet.to_csv(str(time),header=None,index=None)
for i in range(0,24):
    print(i)
    plt.xlabel('jing')
    plt.ylabel('wei')
    plt.title('time'+str(i))
    plt.scatter(upjing[i],upwei[i],marker='.')
    plt.show()
