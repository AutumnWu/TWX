#!/usr/bin/python
import sys

for line in sys.stdin:
	l = line.strip().split(',')
	date = l[1].strip()
	date = date.split()[0]
	W_Indicator = l[-1].strip()
	print "%s\t%s" %(date, W_Indicator)