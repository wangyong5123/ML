from numpy import *

def loadData(filename):
	numFeat = len(open(filename).readline().split('\t')) -1
	dataMat = [];labelMat = []
	fr  = open(filename)
	for line in fr.readline():
		lineArr = []
		curLine = line.strip().split('\t')
		for i in range(numFeat):
			lineArr.append(float(curLine[i]))
		dataMat.append(lineArr)
		lableMat.append(float(curLine[-1]))
	return dataMat,labelMat

def standRegres(xArr,yArr):
	xMat = mat(xArr);yMat = mat(yArr)
	xTx = xMat.T*xMat
	if linalg.det(xTx) == 0.0:
		print("this matrix is singual cannot do inverse")
		return
	ws = xTx.I*(xMat.T*yMat)
	return ws


if __name__ == "__main__":
	xArr,yArr = loadData('ex0.txt')
	ws = standRegres(xArr,yArr)
	print("ws:",ws)
	
	
