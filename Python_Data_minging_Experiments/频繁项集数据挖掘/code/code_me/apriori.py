import pandas as pd
import csv
#加载数据
def loadDataSet():
	#return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
	with open("data1", "r") as csvFile:
		reader = csv.reader(csvFile)
		data = []
		for item in reader:
			data.append(item)
	return data

#创建列表，加入所有的元素
def createC1(dataSet):
	C1 = []
	for transaction in dataSet:
		for item in transaction:
			C1.append([item])
	C1.sort()
	#返回不可变集合
	return map(frozenset, C1)

#大小为1的所有元素的频繁项集，D数据集，候选项集列表ck，最小支持度
def scanD(D, Ck, minSupport):
	ssCnt = {}
	#遍历数据集
	for tid in D:
		#遍历候选项
		for can in Ck:
			#判断候选项中是否包含数据集的各项
			if can.issubset(tid):
				if not can in ssCnt:
					ssCnt[can] = 1
				else:
					ssCnt[can] += 1
	numItems = float(len(D))#数据集的大小
	retList = []#L1初始化
	supportData = {}#记录候选项中各个数据的支持度
	for key in ssCnt:
		support = ssCnt[key]/numItems#计算支持度
		if support >= minSupport:
			retList.insert(0,key) #满足条件加入L1中
		supportData[key] = support
	return retList, supportData

#组合，向上合并
def aprioriGen(Lk,k):#Lk频繁项集列表，项集元素个数k
	retList = []
	lenLk = len(Lk)
	for i in range(lenLk):
		for j in range(i+1, lenLk):#两两遍历组合
			L1 = list(Lk[i])[:k-2]
			L2 = list(Lk[j])[:k-2]
			L1.sort()
			L2.sort()
			if L1 == L2:#若两个集合的前k-2个项相同时，则将连个集合合并
				retList.append(Lk[i] | Lk[j])
	return retList

#apriori算法
def apriori(dataSet, minSupport = 0.5):
	C1 = createC1(dataSet)
	D = list(map(set,dataSet))
	L1, supportData = scanD(D, C1, minSupport)#单项最小支持度判断，生成L1
	L = [L1]#频繁项目集合
	k = 2
	while(len(L[k-2]) > 0):#创建包含更大项集的最大列表，知道下一个大的项集为空
		Ck = aprioriGen(L[k-2], k)#向上合并
		Lk,supK = scanD(D, Ck, minSupport)#单项
		supportData.update(supK)#支持度更新
		L.append(Lk)#
		k+=1
	return L, supportData

#从频繁项集中挖掘关联规则，参数频繁项集列表，包含频繁项集的数据支持度字典，最小可信度阈值
def generateRules(L, supportData, minConf = 0.7):
	bigRuleList = []#可信度规则列表
	for i in range(1,len(L)):
		for freSet in L[i]:
			H1 = [frozenset([item]) for item in freSet]
			if(i > 1):
				rulesFromConseq(freSet,H1,supportData,bigRuleList,minConf)
			else:
				calcConf(freSet, H1, supportData, bigRuleList, minConf)
	return bigRuleList

#对规则进行评估
def calcConf(freSet, H, supportData, br1, minConf = 0.7):
	prunedH = []
	for conseq in H:
		conf = supportData[freSet]/supportData[freSet-conseq]
		if conf >= minConf:
			print(freSet-conseq,'-->',conseq,'conf:',conf)
			br1.append((freSet-conseq,conseq,conf))
			prunedH.append(conseq)
	return prunedH

#生成候选集合
def rulesFromConseq(freSet, H, supportData, br1, minConf = 0.7):
	m = len(H[0])
	if(len(freSet) > (m+1)):
		Hmp1 = aprioriGen(H,m+1)
		Hmp1 = calcConf(freSet,Hmp1,supportData,br1,minConf)
		if(len(Hmp1) > 1):
			rulesFromConseq(freSet,Hmp1,supportData,br1,minConf)

if __name__ == "__main__":
	#创建数据集
	data = loadDataSet()
	#1频繁项集
	#fre1 = createC1(data)
	#1最小支持度
	#retList,support = scanD(data,fre1,0.5)
	L,sup = apriori(data,minSupport=0.2)
	print("频繁项集为：",L)
	print("所有支持度:",sup)
	print("-----")
	print("置信度")
	generateRules(L,sup,0.1)
