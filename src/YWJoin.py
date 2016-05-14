import numpy as np
def join():
	yellowfile = open('yellow_tripdata_2014-04.csv','r')
	trip = yellowfile.readline()
	trip_day = []
	trip_loc = []
	trip_data = []


	#for trip in yellowdata:
	while trip != "":
		trip = trip.strip().split(',')
		if len(trip) != 18:
			pass
		else:
			#trip = trip.strip().split(',')
			if trip[0] == "vendor_id":
				pass
			else:
				#print(trip)
				date = trip[1].split()[0]
				date = date.replace('-','')
				#print ([trip[6],trip[5]])
				location = [trip[6], trip[5]]
				remain_data = trip
				remain_data = ','.join(remain_data)
				trip_day.append(date)
				trip_loc.append(location)
				trip_data.append(remain_data)
		trip = yellowfile.readline()

	weatherfile = open('NYCWeather2014.csv','r')
	weatherdata = weatherfile.read().strip().split('\n')
	station_loc = [[40.77944, -73.88028],[40.77889, -73.96917],[40.63861, -73.76222]]

	weather_dic = {}
	for weather in weatherdata:
		weather = weather.strip().split(',')
		if weather[0] == "STN---":
			pass
		else:
			station_num = weather[0]
			day = weather[2].strip()
			remain_we_data = weather[0:2] + weather[3:]
			remain_we_data = ','.join(remain_we_data)
			if day not in weather_dic:
				weather_dic[day] = {station_num:remain_we_data}
			else:
				weather_dic[day][station_num] = remain_we_data


	outfile = open("YellowWeatherJoin201404.csv",'w')
	for index in range(len(trip_day)):
		day = trip_day[index]
		location = trip_loc[index]
		#print(location)
		lat = float(location[0])
		lon = float(location[1])

		remain = trip_data[index]

		weatherloc1 = station_loc[0]
		weatherloc2 = station_loc[1]
		weatherloc3 = station_loc[2]

		dis1 = (weatherloc1[0]-lat)*(weatherloc1[0]-lat) + (weatherloc1[1]-lon)*(weatherloc1[1]-lon)
		dis2 = (weatherloc2[0]-lat)*(weatherloc2[0]-lat) + (weatherloc2[1]-lon)*(weatherloc2[1]-lon)
		dis3 = (weatherloc3[0]-lat)*(weatherloc3[0]-lat) + (weatherloc3[1]-lon)*(weatherloc3[1]-lon)

		loc_index = np.argmin([dis1,dis2,dis3])

		if loc_index == 0:
			weather = weather_dic[day]['725030']
			outfile.write(remain+','+weather+'\n')
		elif loc_index == 1:
			weather = weather_dic[day]['725053']
			outfile.write(remain+','+weather+'\n')
		else:
			weather = weather_dic[day]['744860']
			outfile.write(remain+','+weather+'\n')

	yellowfile.close()
	weatherfile.close()
	outfile.close()
join()



