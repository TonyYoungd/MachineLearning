"""
    1.降低数据维度
    2.划分出训练集和测试集合
"""

import pandas as pd
dataSet = pd.read_csv("train_part.csv")


"""数据集降维"""
#删除无关特征
del dataSet["custid"]
del dataSet["大类名称"]
del dataSet["中类名称"]
del dataSet["小类编码"]
del dataSet["小类名称"]
del dataSet["销售月份"]
del dataSet["规格型号"]
del dataSet["商品编码"]
del dataSet["商品类型"]



"""处理数据类型"""
#是否促销: 是为1 否为0
for i in range(len(dataSet)):
    if dataSet.ix[i, '是否促销'] == '是':
        dataSet.ix[i, '是否促销'] = 1
    else:
        dataSet.ix[i, '是否促销'] = 0
#单位转化成数值
danwei = list(set(dataSet["单位"]))
print(danwei)
for i in range(len(dataSet)):
    for a, b in enumerate(danwei):
        if dataSet.ix[i, '单位'] == b:
            dataSet.ix[i, '单位'] = a
"""
#商品编码
for i in range(len(dataSet)):
    dataSet.ix[i, '商品编码'] = dataSet.ix[i, '商品编码'][4:]
"""


"""划分训练集"""
#划分训练集和测试集
data_train = dataSet.ix[:len(dataSet)*(3/4)]
data_test = dataSet.ix[len(dataSet)*(3/4):]
#训练集特征和结果
data_train_y = data_train["销售数量"]
data_train_y.to_csv("data_train_y.csv", index=None, header=None)
del data_train["销售数量"]
data_train.to_csv("data_train_x.csv", index=None, header=None)
#测试集特征和结果：
data_test_y = data_test["销售数量"]
data_test_y.to_csv("data_test_y.csv", index=None, header=None)
del data_test["销售数量"]
data_test.to_csv("data_test_x.csv", index=None, header=None)