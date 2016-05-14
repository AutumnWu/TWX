#!/usr/bin/python
import sys
import math

for line in sys.stdin:
	l = line.strip().split(',')
	date = l[1].strip()
	date = date.split()[0]
	W_Indicator = l[-1].strip()
	try:
		tip_amount = float(l[15].strip())
		total_amount = float(l[18].strip())
		print "%s\t%s\t%d\t%d" %(date,W_Indicator,tip_amount,total_amount)
	except:
		continue