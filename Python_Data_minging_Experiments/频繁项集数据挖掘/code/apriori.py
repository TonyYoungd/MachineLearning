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
	print("loaddata over")
	return data


def createC1(dataSet):
	C1 = []
	for transaction in dataSet:
		for item in transaction:
			C1.append([item])
	C1.sort()
	print("creat over")
	return list(map(frozenset, C1))

def scanD(D, Ck, minSupport):
	ssCnt = {}
	for tid in D:
		for can in Ck:
			if can.issubset(tid):
				if not can in ssCnt:
					ssCnt[can] = 1
				else:
					ssCnt[can] += 1
	numItems = float(len(D))
	retList = []
	supportData = {}
	for key in ssCnt:
		support = ssCnt[key]/numItems
		if support >= minSupport:
			retList.insert(0,key)
		supportData[key] = support
	return retList, supportData
def aprioriGen(Lk,k):
	retList = []
	lenLk = len(Lk)
	for i in range(lenLk):
		for j in range(i+1, lenLk):
			L1 = list(Lk[i])[:k-2];L2 = list(Lk[j])[:k-2]
			L1.sort();L2.sort()
			if L1 == L2:
				retList.append(Lk[i] | Lk[j])
	return retList
def apriori(dataSet, minSupport = 0.5):
	C1 = createC1(dataSet)
	D = list(map(set,dataSet))
	L1, supportData = scanD(D, C1, minSupport)
	L = [L1]
	k = 2
	while(len(L[k-2]) > 0):
		Ck = aprioriGen(L[k-2], k)
		Lk,supK = scanD(D, Ck, minSupport)
		supportData.update(supK)
		L.append(Lk)
		k+=1
	return L, supportData

#从频繁项集中挖掘关联规则，求置信度
def generateRules(L, supportData, minConf = 0.7):
	bigRuleList = []
	for i in range(1,len(L)):
		for freSet in L[i]:
			H1 = [frozenset([item]) for item in freSet]
			if(i > 1):
				rulesFromConseq(freSet,H1,supportData,bigRuleList,minConf)
			else:
				calcConf(freSet, H1, supportData, bigRuleList, minConf)
	return bigRuleList
def calcConf(freSet, H, supportData, br1, minConf = 0.7):
	prunedH = []
	for conseq in H:
		conf = supportData[freSet]/supportData[freSet-conseq]
		if conf >= minConf:
			print(freSet-conseq,'-->',conseq,'conf:',conf)
			br1.append((freSet-conseq,conseq,conf))
			prunedH.append(conseq)
	return prunedH

def rulesFromConseq(freSet, H, supportData, br1, minConf = 0.7):
	m = len(H[0])
	if(len(freSet) > (m+1)):
		Hmp1 = aprioriGen(H,m+1)
		Hmp1 = calcConf(freSet,Hmp1,supportData,br1,minConf)
		if(len(Hmp1) > 1):
			rulesFromConseq(freSet,Hmp1,supportData,br1,minConf)


def run_main():
	dataSet = loadDataSet()
	print("数据集为：",dataSet)
	print("数据集的长度为",len(dataSet))
	L,support = apriori(dataSet,0.2)
	print("频繁项集为：",L)
	print("所有的支持度为：",support)








if __name__ == "__main__":
	run_main()