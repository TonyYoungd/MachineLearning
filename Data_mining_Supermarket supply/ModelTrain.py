"""
    训练模型：
        1.获取数据
        2.训练模型（SVR）
	3.保存模型

"""

from sklearn import svm
import csv
from sklearn.externals import joblib

"""加载数据"""
#获取数据保存在列表中
data_train_x = []
data_train_y = []
data_test_x = []
data_test_y = []
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

"""训练模型"""

#SVR模型
clf = svm.SVR()
clf.fit(data_train_x, data_train_y)
#保存模型
joblib.dump(clf, "train_model_SVM.m")
#result = clf.predict(data_test_x)
#print("测试结果：", result)
