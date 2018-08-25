#导入数据集
import csv
def getData():
    #age年龄段 spetacle 近视 远视力前 astigmatic散光，tear泪液，类
    labels = ['age','spetacle','astigmatic','tear']
    with open("../data/data_p.csv","r") as csvFile:
        reader = csv.reader(csvFile)
        data = []
        for item in reader:
            data.append(item)
            for example in data:
                for index in range(4):
                    example[index] = int(example[index])
    return data,labels
def getData_t():
    labels = ['age', 'spetacle', 'astigmatic', 'tear']
    with open("../data/data_t.csv", "r") as csvFile:
        reader = csv.reader(csvFile)
        data = []
        for item in reader:
            data.append(item)
        for example in data:
            for index in range(4):
                example[index] = int(example[index])
    return data,labels




