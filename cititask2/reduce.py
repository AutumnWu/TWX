#!/Users/xnameispenguin/anaconda2/bin/python
import sys

R_trip_count = [0 for i in range(11)]
R_date = [[] for i in range(11)]

Snow_trip_count = [0 for i in range(11)]
Snow_date = [[] for i in range(11)]

Sunny_trip_count = [0 for i in range(11)]
Sunny_date = [[] for i in range(11)]

for line in sys.stdin:
	l = line.strip().split('\t')
	date = l[0]
	W_indicator = l[1]
	dis_section = int(l[2])
	#print dis_section
	if W_indicator[1] == "1" or W_indicator[4] == "1":

		#if dis_section in R_trip_count:
		R_trip_count[dis_section-1] += 1

		if date not in R_date[dis_section-1]:
			R_date[dis_section-1].append(date)


	if W_indicator[2] == "1" or W_indicator[3] == "1":

		Snow_trip_count[dis_section-1] += 1

		if date not in Snow_date[dis_section-1]:
			Snow_date[dis_section-1].append(date)

	if W_indicator == "000000":

		Sunny_trip_count[dis_section-1] += 1

		if date not in Sunny_date[dis_section-1]:
			Sunny_date[dis_section-1].append(date)

R_pri = []
Snow_pri = []
Sunny_pri = []
for i in range(11):
	R_pri.append(str(R_trip_count[i]))
	R_pri.append(str(len(R_date[i])))
	Snow_pri.append(str(Snow_trip_count[i]))
	Snow_pri.append(str(len(Snow_date[i])))
	Sunny_pri.append(str(Sunny_trip_count[i]))
	Sunny_pri.append(str(len(Sunny_date[i])))

print ','.join(R_pri)
print ','.join(Snow_pri)
print ','.join(Sunny_pri)
