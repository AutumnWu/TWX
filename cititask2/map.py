#!/Users/xnameispenguin/anaconda2/bin/python
import sys
import math
from math import radians, cos, sin, asin, sqrt

# import googlemaps
#
#
#
# triplist=list()
# distlist=list()
# dist=0
# gmaps = googlemaps.Client(key='AIzaSyCE23MdFLCeokwSTL_f3ghC-t8eMcYbBcg',timeout=None)
# for line in sys.stdin:
#     line = line.strip().split(',')
#     date = line[0]
#     start=float(line[7]) float(line[8])
#     end= float(line[11]) float(line[12])
#     print start,end
# start=(40.74177603,-74.00149746)
# end=(40.73726186,-73.99238967)
# directions_result = gmaps.distance_matrix((40.74177603,-74.00149746),(40.73726186,-73.99238967),mode="bicycling")
    # trip = [start,end]
    # if trip not in triplist:
    #     triplist.append((trip))
    #     # directions_result = gmaps.directions(start,end,mode="bicycling")
    # directions_result = gmaps.distance_matrix(start,end,mode="bicycling")
    # dist=directions_result.get('rows')[0].get('elements')[0].get('distance').get('value') #unit meters
    # dist= 0.000621371192237 *dist #unit miles
    # print dist
    #     disttuple = [start,end,dist]
    #     distlist.append((disttuple))
    # else:
    #     for item in distlist:
    #         if item[0]==start and item[1]==end:
    #             dist= item[2]

def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

for line in sys.stdin:
    line = line.strip().split(',')
    date = line[0]
    start=float(line[7]), float(line[8])
    end= float(line[11]), float(line[12])
    dist=haversine(start[0],start[1],end[0],end[1])
    section = int(math.ceil(dist))
    if section > 10:
		section = 11
    print "%s\t%s\t%d" %(date,line[-1],section)



# start=(40.74177603, -74.00149746)
# end=(40.73726186, -73.99238967)
    # if  dist <= 0.25:
    #     dist = 0.25
    # elif dist <= 0.5:
    #     dist = 0.5
    # elif dist <= 0.75:
    #     dist= 0.75
    # elif dist <= 1:
    #     dist = 1
    # elif dist <= 1.25:
    #     dist= 1.25
    # elif dist<= 1.5:
    #     dist = 1.5
    # elif dist <= 1.75:
    #     dist= 1.75
    # elif dist <= 2:
    #     dist = 2
    # elif dist <= 2.25:
    #     dist= 2.25
    # elif dist<=2.5:
    #     dist = 2.5
    # elif dist <= 2.75:
    #     dist= 2.75
    # elif dist <= 3:
    #     dist = 3
    # elif dist <= 3.25:
    #     dist= 3.25
    # elif dist<=3.5:
    #     dist = 3.5
    # else:
    #     dist=3.51
    # if  dist <=1:
    #     dist = "[0,1]"
    # elif dist <= 2:
    #     dist = "(1,2]"
    # elif dist <= 3:
    #     dist= "(2,3]"
    # elif dist<=4:
    #     dist ="(3,4]"
    # elif dist <=5:
    #     dist="(4,5]"
    # elif dist <=6:
    #     dist="(5,6]"
    # elif dist <=7:
    #     dist = "(6,7]"
    # elif dist <=8:
    #     dist ="(7,8]"
    # elif dist <=8:
    #     dist = "(8,9]"
    # elif dist <=9:
    #     dist = "(9,10]"
    # else:
    #     dist ="above 10 miles"
    # print "%s\t%s\t%s" %(date,line[36],dist)
