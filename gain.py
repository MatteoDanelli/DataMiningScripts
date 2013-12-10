#Claculate information gain for two-class problems

import sys
import math
from itertools import izip

def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

def l2(x):
	return math.log(x,2)

def entropyA(array):
	entropy=0
	for i in range(len(array)):
		if array[i]==0:
			break;
		else:
			entropy=entropy-array[i]*l2(array[i])
	return entropy

def infoA(list):
	s=sum(list)
	a=[]
	for i in list:
		a.append(i/s)
	return entropyA(a)

print "\tInfo Gain for 2-class problem"

print "Insert values BEFORE split (separated by space): "
valueBefore=[]
valueBefore = map (float, sys.stdin.readline().split())
infoBefore=infoA(valueBefore)

print "Insert values AFTER split (separated by space): "
valueAfter=[]
valueAfter = map(float,sys.stdin.readline().split())
total=sum(valueAfter)
infoAfter=0
for i,j in pairwise(valueAfter):
	temp=[]
	temp.append(i)
	temp.append(j)
	infoAfter=infoAfter + (i+j)/total * infoA(temp)
gain=infoBefore-infoAfter

print "Result gain= " + str("{0:.3f}".format(gain))
