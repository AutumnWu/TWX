#!/usr/bin/python
import sys
import math
import json


class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Polygon:
	def __init__(self,points):
		self.points = points
		self.nvert = len(points)
		minx = maxx = points[0].x
		miny = maxy = points[0].y
		for i in xrange(1,self.nvert):
			minx = min(minx,points[i].x)
			miny = min(miny,points[i].y)
			maxx = max(maxx,points[i].x)
			maxy = max(maxy,points[i].y)
		self.bound = (minx,miny,maxx,maxy)
	def contains(self,pt):
		firstX = self.points[0].x
		firstY = self.points[0].y
		testx = pt.x
		testy = pt.y
		c = False
		j = 0
		i = 1
		nvert = self.nvert
		while (i < nvert) :
			vi = self.points[i]
			vj = self.points[j]
			if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
				c = not(c)
			if(vi.x == firstX and vi.y == firstY):
				i = i + 1
				if (i < nvert):
					vi = self.points[i];
					firstX = vi.x;
					firstY = vi.y;
			j = i
			i = i + 1
		return c
	def bounds(self):
		return self.bound


polygon=[]
with open('/Users/xnameispenguin/Dropbox/study/NYU/BIg_Data/project/zippolygon.json') as data_file:
    data = json.load(data_file)
    data= data['features']#convert to list
    for item in data:
        zipcode=item['properties']['@id'][-5:]
        cordinates=item['geometry']['coordinates'][0]
        points=[]
        for pt in cordinates:
            p=Point(pt[1],pt[0])
            points.append(p)
        poly= Polygon(points)
        polygon.append([poly,zipcode])

for ln in sys.stdin:

    ln = ln.strip().splitlines()
    for line in ln:
        line =line.strip().split(',')
        zipcode=0

        if len(line)==3:
            if line[0]!="Geography":
                zipcode=line[0][-5:]
                income=line[1]
                print ('%s\tL|%s' %(zipcode,income ))
        else:
            try:
                start=Point(float(line[7]),float(line[8]))#starting cordinates
            except ValueError:
                continue
            for item in polygon:
                shape=item[0]
                if  shape.contains(start):
                    zipcode=item[1]
                    print ('%s\tR|t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' %(zipcode,line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32],line[33],line[34],line[35],line[36] ))
