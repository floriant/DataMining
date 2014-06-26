import numpy as np
x = np.arange(9).reshape((3,3))
y = np.arange(3)

print x
print y

print np.dot(x,y)
print "------------------------------"

x1 = np.matrix("0,1,2; 3,4,5; 6,7,8")
x2 = np.matrix("0,1,2")

x2t = x2.T

print x1*x2t

print "------------------"

xTest = np.arange(9).reshape((3,3))
xTrans = np.transpose(xTest)
print xTest
print xTrans