import apriori
from GetData import changeData,handleData
def run_main():
	#处理数据
	#changeData()
	#handleData()
	#测试频繁项集
	dataSet = apriori.loadDataSet()
	print(dataSet)
	print(len(dataSet))
	#C1 = apriori.createC1(dataSet)
	#D = list(map(set,dataSet))
	L,suppData = apriori.apriori(dataSet,0.2)
	print(L)
	print("========")
	print(L[0])

	#print("========")
	#print(L[1])
	#print("========")
	#confidence
	#L,suppData = apriori.apriori(dataSet,minSupport=0.5)
	#print(L[0])
	#print(suppData)
	#rules = apriori.generateRules(L,suppData,minConf=0.1)
	#print(rules)
	#rules = apriori.generateRules(L,suppData,minConf=0.5)
	#print(rules)





if __name__ == "__main__":
	run_main()
