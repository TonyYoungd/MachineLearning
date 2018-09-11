"""
    对data/data_new/中的数据进行画图
    每个小时的行车数据
    每个时间段所有的出租车行驶路线成一图
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
loc = "../data/data_new/"
dirs = os.listdir(loc)
for i in dirs:
    print(i)
    dataSet = pd.read_csv(loc+i, header=None)
    x = dataSet[3]
    y = dataSet[4]
    plt.title(i)
    plt.plot(x, y, color='r')
    plt.show()
