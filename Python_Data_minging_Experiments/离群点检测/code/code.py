#基于距离的利群点的分析
import math
import scipy.io as sio
import matplotlib.pyplot as plt
def getData():
    data1 = sio.loadmat("../data/data1.mat")
    data = data1.get("Xval")
    return data

#计算两点间的欧式距离
def dist(x,y):
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    dis = math.sqrt((a-c)*(a-c)+(b-d)*(b-d))
    return dis
#数据集，距离阈值，分数阈值;
def outlier(dataSet,r,pi):
    n = len(dataSet)
    for i in range(1,n):
        count = 0
        for j in range(1,n):
            if i != j and dist(dataSet[i],dataSet[j]) <= r:
                count += 1
                if count >= pi*n:
                    #print("{}不可能是DB(r,pi)-离群点".format(dataSet[i]))
                    break
        print("{}是离群点".format(dataSet[i]))
def run_main():
    r = 10
    pi = 0.9
    data = getData()
    outlier(data,r,pi)

if __name__ == "__main__":
    run_main()
