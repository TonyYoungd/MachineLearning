#读取数据
import os
import pandas as pd
def changeData():
    path1 = "text1"
    path2 = 'text2'
    filelist = os.listdir(path1)
    for files in filelist:
        Olddir = os.path.join(path1,files)
        filename = os.path.splitext(files)[0]
        filetype = os.path.splitext(files)[1]
        print(Olddir)
        file_test = open(Olddir,'r')
        Newdir = os.path.join(path2,str(filename)+'.csv')
        print(Newdir)
        file_test2 = open(Newdir,'w')
        for lines in file_test.readlines():
            strdata = ",".join(lines.split('\t'))
            file_test2.write(strdata)
        file_test.close()
        file_test2.close()

#数据提取
def handleData():
    data = pd.read_csv("text2/ratings.csv",sep="::",header=None)
    rate = data[data[2] > 3]
    users = set(rate[0])
    for user in users:
        df = pd.DataFrame({'A':rate[rate[0]==user][1]})
        df.T.to_csv('data1.csv', header=None, index=False,mode="a")