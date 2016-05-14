#!/usr/bin/python
import sys

R_date = []
R_total_amount = 0
R_tip_amount = 0

Snow_date = []
Snow_total_amount = 0
Snow_tip_amount = 0

Sunny_date = []
Sunny_total_amount = 0
Sunny_tip_amount = 0


for line in sys.stdin:
	l = line.strip().split('\t')
	date = l[0]
	W_indicator = l[1]
	tip_amount = float(l[2])
	total_amount = float(l[3])

	if W_indicator[1] == "1" or W_indicator[4] == "1":
		R_tip_amount += tip_amount
		R_total_amount += total_amount
		if date not in R_date:
			R_date.append(date)

	if W_indicator[2] == "1" or W_indicator[3] == "1":
		Snow_tip_amount += tip_amount
		Snow_total_amount += total_amount
		if date not in Snow_date:
			Snow_date.append(date)

	if W_indicator == "000000":
		Sunny_tip_amount += tip_amount
		Sunny_total_amount += total_amount
		if date not in Sunny_date:
			Sunny_date.append(date)

print str(Sunny_tip_amount) + ',' + str(Sunny_total_amount) + ',' +str(len(Sunny_date))+','+str(R_tip_amount) + ',' + str(R_total_amount) + ',' + str(len(R_date)) + ','+str(Snow_tip_amount) + ',' + str(Snow_total_amount) + ','+str(len(Snow_date))
	


