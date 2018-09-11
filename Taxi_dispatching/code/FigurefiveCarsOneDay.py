"""
    随机五辆车一天的路线行驶图
"""
import pandas as pd
import matplotlib.pyplot as plt

#路线
loc = "../data/Taxi_070220/"
dataSet = pd.read_csv(loc+"Taxi_106", header=None)
x = dataSet[2]
y = dataSet[3]
#画曲线图
plt.plot(x, y, color="r")

dataSet = pd.read_csv(loc+"Taxi_105", header=None)
x = dataSet[2]
y = dataSet[3]
plt.plot(x, y, color="b")

dataSet = pd.read_csv(loc+"Taxi_109", header=None)
x = dataSet[2]
y = dataSet[3]
plt.plot(x, y, color="black")

dataSet = pd.read_csv(loc+"Taxi_117", header=None)
x = dataSet[2]
y = dataSet[3]
plt.plot(x, y, color="g")

dataSet = pd.read_csv(loc+"Taxi_107", header=None)
x = dataSet[2]
y = dataSet[3]
plt.plot(x, y, color="y")

plt.title('5 cars one day')




plt.show()




