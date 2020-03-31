import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth",fc="0.8")
leafNode = dict(boxstyle="round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")

def getNumLeafs(myTree):
	numLefts = 0;
	firstStr = myTree.key()[0]
	secondDict = myTree[firstStr]

	for key in secondDict.keys():
		if type(secondDict[key]).__name__ =='dict':
				numLeafs += getNumLeafs(secondDict[key])

		else:
			numLeafs += 1

	return numLeafs

def getTreeDepth(myTree):
	maxDepth = 0;
	firstStr = myTree.keys()[0]

	secondDict = myTree[firstStr]

	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			thisDepth = 1+getTreeDepth(secondDict[key])
		else:
			thisDepth=1

		if thisDepth > maxDepth:maxDepth = thisDepth
	return maxDepth


def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	createPlot.axl.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',xytext=centerPt,textcoords='axes fraction',\
	va = "Center",ha="center",bbox=nodeType,arrowprops=arrow_args)



def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.axl.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )
 

def createPlot():
	fig = plt.figure(1,facecolor = 'white')
	fig.clf()
	createPlot.axl = plt.subplot(111,frameon=False)
	plotNode('jue ce dian',(0.5,0.1),(0.1,0.5),decisionNode)
	plotNode('ye jie dian',(0.8,0.1),(0.3,0,8),leafNode)
	plt.show()



def main():
	createPlot()

if __name__ == "__main__":
	main()
