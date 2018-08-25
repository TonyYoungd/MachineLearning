from math import log
import operator
from GetData import getData
#创建数据
def createDataSet():
    return getData()
#计算信息熵
def calcShannonEnt(dataSet):
    #计算数据集中实例的总数
    numEntries = len(dataSet)
    #创建字典键存放数据的分类，值记录了当前类别出现的次数
    labelCounts = {}
    #向字典中添加数据
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    #计算信息熵
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt
#按照给定的特征划分数据集
def splitDataSet(dataSet, axis, value):#待划分的数据集，划分数据集的特征，需要返回的特征值
    #存储划分好的数据
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet
#选择最好的数据集划分方式，计算得出最好的划分数据集的特征
def chooseBestFeatureToSplit(dataSet):
    #保存一行数据的所有特征的个数
    numFeatures = len(dataSet[0]) - 1
    #计算数据集的信息熵
    baseEntropy = calcShannonEnt(dataSet)
    #最佳信息增益
    bestInfoGain = 0.0
    #最佳划分特征
    bestFeature = -1
    #遍历数据集中所有的特征
    for i in range(numFeatures):
        #保存特征列表
        featList = [example[i] for example in dataSet]
        #转化为集合去重
        uniqueVals = set(featList)
        #新的信息熵
        newEntropy = 0.0
        #遍历当前特征中的所有唯一的属性
        for value in uniqueVals:
            #切割数据集
            subDataSet = splitDataSet(dataSet,i,value)
            #对所有计算的新的信息熵求和
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        #计算增益信息
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
        #返回最佳划分特征
        return bestFeature
#递归构建决策树
def createTree(dataSet,labels):#数据集和标签列表
    #保存所有的分类
    classList = [example[-1] for example in dataSet]
    #递归出口1.所有的类标签完全相同，则直接返回该类标签
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    #递归出口2.使用完了所有的特征仍然无法简单的返回唯一的类标签
    if len(dataSet[0]) == 1:
        return majorituCnt(classList)
    #选择最佳特征及其标签
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    #定义决策数
    myTree = {bestFeatLabel:{}}
    #在标签列表中删除最佳特征
    del(labels[bestFeat])
    #选择最佳特征的值的类型
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for values in uniqueVals:
        #剪除此标签
        subLabels = labels[:]
        myTree[bestFeatLabel][values] = createTree(splitDataSet(dataSet,bestFeat,values),subLabels)
    return myTree
#多数表决
def majorituCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
#使用决策数进行分类
def classify(inputTree,featLabels,testVec):
    classLabel = ""
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key],featLabels,testVec)
            else:
                classLabel = secondDict[key]
    return classLabel