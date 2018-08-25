"""
    预测数据四月份的数据：
        目标格式：编码 日期 销量

"""

from sklearn.externals import joblib
import pandas as pd

#加载模型
clf = joblib.load("train_model_SVM.m")

#查看数据
dataSet = pd.read_csv("data_train_x.csv", header=None)
print(dataSet)