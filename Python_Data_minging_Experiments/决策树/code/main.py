from tree import createDataSet,calcShannonEnt,splitDataSet,createTree,classify
from GetData import getData_t
def run_main():
	#创建数据集
	myDat,labels = createDataSet()
	labelss = labels[:]
	print("数据集为:",myDat)
	#计算熵
	#print("熵：{}".format(calcShannonEnt(myDat)))
	#划分数据集
	#print(splitDataSet(myDat,0,1))
	myTree = createTree(myDat,labels)
	print("所构造的决策树为",myTree)
	#splitDataSet(myDat,0,1)print("--")
	data,labels = getData_t()
	result = []
	for example in data:
		result.append(classify(myTree,labels,example))
	print("所属于的分类为",result)










if __name__ == "__main__":
	run_main()