#Script to calculate log base 2 of any number.

import sys
import math
while(1):
	print "Insert value: "
	x=float(sys.stdin.readline())
	print math.log(x,2) 
