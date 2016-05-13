#!/usr/bin/python
import sys

R_trip_count = 0
R_date = []
Snow_trip_count = 0
Snow_date = []
Sunny_trip_count = 0
Sunny_date = []

for line in sys.stdin:
	l = line.strip().split('\t')
	date = l[0]
	W_indicator = l[1]
	if W_indicator[1] == "1" or W_indicator[4] == "1":
		R_trip_count += 1
		if date not in R_date:
			R_date.append(date)
	if W_indicator[2] == "1" or W_indicator[3] == "1":
		Snow_trip_count += 1
		if date not in Snow_date:
			Snow_date.append(date)
	if W_indicator == "000000":
		Sunny_trip_count += 1
		if date not in Sunny_date:
			Sunny_date.append(date)


print str(Sunny_trip_count) + ',' +str(len(Sunny_date))+','+str(R_trip_count) + ',' + str(len(R_date)) + ','+str(Snow_trip_count) + ','+str(len(Snow_date))
		