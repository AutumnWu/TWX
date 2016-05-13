#!/usr/bin/python
import sys
import math

for line in sys.stdin:
	l = line.strip().split(',')
	date = l[1].strip()
	date = date.split()[0]
	W_Indicator = l[-1].strip()
	distance = float(l[4].strip())
	section = int(math.ceil(distance))
	if section <= 0:
		continue
	if section > 10:
		section = 11
	print "%s\t%s\t%d" %(date,W_Indicator,section)


