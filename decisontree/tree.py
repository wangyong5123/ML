from math import log
import operator
#/*choose best data split way*/

def createTree(dataSet,labels):
	classList = [example[-1] for example in dataSet]
	
	print(classList.count(classList[0]),len(classList))

	if classList.count(classList[0]) == len(classList):
		return classList[0]

	print('len',len(dataSet[0]))
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)

	bestFeat = chooseBestFeatureToSplit(dataSet)
#	print('bestFeat:',bestFeat)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}

	print('myTree',myTree)	
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	print('featValues',featValues)
	uniqueVals = set(featValues)

	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
	return myTree

def majority(classList):
	classCount={}
	for vote in classList:
		if vote not in classCount.keys():classCount[vote]=0
		classCount[vote] += 1
	sortedClassCount =  sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	print('sortedClassCount:',sortedClassCount)
	return sortedClassCount[0][0]
	

def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1
#	print('numFeatures:',numFeatures)

	baseEntropy = calcShannonEnt(dataSet)
#	print('baseEntropy:',baseEntropy)
	bestInfoGain = 0.0;bestFeature = -1

	for i in range(numFeatures):
#		print('##################################i count',i)
		featList = [example[i] for example in dataSet]
	
#		print('featList:',featList)	
		uniqueVals = set(featList)
#		print('uniqueVals:',uniqueVals)
		newEntropy = 0.0
		
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet,i,value)
#			print('subDataSet',subDataSet)
			#print('len:%d,%d',len(subDataSet),len(dataSet))
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
			#print('newEntropy:',newEntropy)
			

#		print('newEntropy',newEntropy)		
		
		infoGain = baseEntropy - newEntropy

#		print('infoGain:',infoGain);
		if(infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	
	return bestFeature


    


def splitDataSet(dataSet,axis,value):
	retDataSet = []
	for featVec in dataSet:
#		print('#######################q2:%d,%d',featVec[axis],value)
		if featVec[axis] == value:
			print('fetVec:',featVec,axis)
			reducedFeatVec = featVec[:axis]
		#	print('q1:',reducedFeatVec)
			reducedFeatVec.extend(featVec[axis+1:])
		#	print('q2',reducedFeatVec);
			retDataSet.append(reducedFeatVec)
	return	retDataSet

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		print('featVec',featVec)
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] +=1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob * log(prob,2)

	return shannonEnt


def createDataSet():
	dataSet = [[1,1,'yes'],
		[1,1,'yes'],
		[1,0,'no'],
		[0,1,'no'],
		[0,1,'no']
	]
	labels = ['no surfacing','flippers']
	return dataSet,labels
def main():
	myMat,labels = createDataSet()
	print(myMat)
#	ret = splitDataSet(myMat,0,0)
#	print(ret)

#	value = calcShannonEnt(myMat)
#	print(value)

#	ret = chooseBestFeatureToSplit(myMat)	     
#	print(ret)


#	ret = createTree(myMat,labels)
#	print(ret)

	fr = open('lenses.txt')
	lenses=[inst.strip().split('\t') for inst in fr.readlines()]

	lensesLables = ['age','prescript','astigmatic','tearRate']
	lensesTree = createTree(lenses,lensesLables)
	
	print('lensesTree:',lensesTree)

if __name__ == "__main__":
    main()
