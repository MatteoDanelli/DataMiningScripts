import sys
import math

def l2(x):
	return math.log(x,2)

def entropy(array):
	entropy=0
	for i in range(len(array)):
		if array[i]==0:
			break;
		else:
			entropy=entropy-array[i]*l2(array[i])
	return entropy

def info(list):
	s=sum(list)
	a=[]
	for i in list:
		a.append(i/s)
	return entropy(a)

while(1):
	print "Insert value of Info: "
	x=[]
	x=map(float,sys.stdin.readline().split())
	print "{0:.3f}".format(info(x))
