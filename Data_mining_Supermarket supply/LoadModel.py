"""
    加载模型
    测试结果
"""

from sklearn.externals import joblib
import csv
import numpy as np
import pandas as pd

#加载模型
clf = joblib.load("train_model_SVM.m")
#加载测试集合
data_test_x = []
data_test_y = []
data_train_x = []
data_train_y = []
with open("data_test_y.csv") as test:
    data = csv.reader(test)
    for item in data:
        if len(item) == 0:
            item.append('0')
        data_test_y.append(item[0])
with open("data_test_x.csv") as train:
    data = csv.reader(train)
    for item in data:
        data_test_x.append(item)
with open("data_train_x.csv") as train:
    data = csv.reader(train)
    for item in data:
        data_train_x.append(item)
with open("data_train_y.csv") as test:
    data = csv.reader(test)
    for item in data:
        if len(item) == 0:
            item.append('0')
        data_train_y.append(item[0])

#测试
result = []
tmp = clf.predict(data_test_x)
for i in tmp:
    result.append(str(i))
print("测试结果:", result)
print("真实结果：", data_train_y)

#RMSE误差判断
sum_mean = 0
for i in range(len(result)):
    sum_mean += (float(result[i])-float(data_test_y[i]))**2
score = np.sqrt(sum_mean/len(result))
print("RMSE by hand:", score)

#保存结果
result = pd.DataFrame(result)
data = pd.read_csv("data_test_x.csv")
data[7] = result
data.to_csv("Answer.csv", index=None, header=None)
