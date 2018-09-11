#!/bin/python
import pandas as pd
import os


#将所有文件的数据整合到一个文件，保存在taxidata文件中
dirname=os.listdir('/home/alin/Downloads/taxi/Taxi_070220')
fout=open(r'/home/alin/taxidata','a+')
for filename in dirname:
	fopen=open(r'/home/alin/Downloads/taxi/Taxi_070220/'+filename,'r')
	lines=[]
	lines=fopen.read()
	fopen.close()
	for line in lines:
		fout.write(line)
		
#找出乘客状态发生变化的数据，保存在aaaa.csv文件		
fp=pd.read_csv(r'/home/alin/taxi/taxidata',header=None)
f6=fp[6].values

for i in range(len(f6)):
	if f6[i] != f6[i+1]:
		#print(fp.ix[i, :])
		#print(fp.ix[i+1, :])
		df1 = pd.DataFrame(fp.ix[i, :])
		df1.T.to_csv('aaaa.csv', header=None, index=False, mode = 'a')
		df2 = pd.DataFrame(fp.ix[i+1, :])
		df2.T.to_csv('aaaa.csv', header=None, index=False, mode = 'a')

		
		
#整理出下车数据和上车数据，分别保存在pick.csv和getup.csv中
fp=pd.read_csv('/home/alin/taxi/aaaa.csv',header=None)


f6=fp[6].values
for i in range(len(f6)):
	if f6[i]==0 and f6[i+1]!=0:
		df1=pd.DataFrame(fp.ix[i+1,:])
		df1.T.to_csv('getup.csv',header=None,index=False,mode='a')
	elif f6[i]!=0 and f6[i+1]==0:
		df2=pd.DataFrame(fp.ix[i+1,:])
		df2.T.to_csv('pick.csv',header=None,index=False,mode='a')
