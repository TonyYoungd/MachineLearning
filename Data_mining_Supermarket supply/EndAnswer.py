"""
    处理预测结果，得到最终格式的文件
"""
import pandas as pd
#读取结果
dataSet = pd.read_csv("Answer.csv", header=None)
print(dataSet)

#处理大类
dataSet[[0, 2, 7]].groupby([0, 2])[[7]].sum().to_csv('Answer_dalei.csv', header=None)
#处理中类
dataSet[[1, 2, 7]].groupby([1, 2])[[7]].sum().to_csv("Answer_zhonglei", header=None)




