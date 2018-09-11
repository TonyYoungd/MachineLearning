"""
    画出所有的车一天的行驶轨迹图
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
loc = "../data/Taxi_070220/"
dirs = os.listdir("../data/Taxi_070220")
plt.title("all")

for i in dirs:
    dataSet = pd.read_csv(loc+i, header=None)
    x = dataSet[2]
    y = dataSet[3]
    plt.plot(x, y, color='r', )
plt.show()




