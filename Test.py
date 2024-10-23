import numpy as np
import KNN
from importlib import reload
import matplotlib
import matplotlib.pyplot as plt

'''
2.2.2
group,labels = KNN.createDataSet()
reload(KNN)
datingDataMat,datingLabels = KNN.file2matrix('datingTestSet.txt')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2],
         15.0*np.array(datingLabels), 15.0*np.array(datingLabels) )
plt.show()
'''

'''
#2.2.3
reload(KNN)
datingDataMat,datingLabels = KNN.file2matrix('datingTestSet.txt')
normMat, ranges,minVals = KNN.autoNorm(datingDataMat)
print(minVals)
'''

'''
reload(KNN)
testVector = KNN.img2vector('testDigits/0_13.txt')
print(testVector[0,0:31])
print(testVector[0,32:63])
'''

reload(KNN)
print(KNN.handwritingClassTest())





























