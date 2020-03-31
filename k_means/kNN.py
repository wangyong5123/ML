from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']

	return group,labels

def classify0(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0]
	print('dataSize:',dataSetSize)

	diffMat = tile(inX,(dataSetSize,1)) - dataSet

	print('diffMat:',diffMat)
	sqDiffMat = diffMat**2#each one 2
	print('sqDif:',sqDiffMat)

	sqDistances = sqDiffMat.sum(axis=1)
	print('sqDistances:',sqDistances)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	print('sorted:',sortedDistIndicies)
	classCount={}
	
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		print('vote:',voteIlabel)

		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
		#print('',classCount[])
		print('items',classCount.items())
		sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]


if __name__ == '__main__':

	dataSet,labels = createDataSet()
	input = array([1.1,0.3])
	K = 3
	output = classify0(input,dataSet,labels,K)
	print("测试数据为:",input,"分类结果为：",output)
