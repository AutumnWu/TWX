Big Data Final Project

Chen Tong
chentong@nyu.edu
ct1897

Jing Xie
jx375@nyu.edu
jx375

Yanqiu Wu
yanqiu.wu@nyu.edu
yw1370

# Project Name:
TWX short for Taxi With X
 
The project report should have the following information
• Title
• Authors
• Abstract: The idea of the abstract is to provide a brief summary of
the report. It should give the reader an idea about the work that was undertaken
and what you findings are. 
• Introduction: This is where you need to outline the motivation for
your work, state the problem you are addressing, why is important, the underlying concepts, and justify if and how big data infrastructure was needed (or useful) for your project.
• Experimental techniques and methods: You should provide details about the methodology and  tools you used. You should also describe your experimental setup, including the data you used,
and the cluster configuration (e.g., node configuration, number of nodes, mappers and reducers)
• Results and discussion: Discuss your findings as well as any issues/challenges
you encountered and how you addressed them.
• Individual Contributions: describe the contributions each member of group made to the project
• Summary/conclusions
• References: List any references you have used

# Timeline

## April 10th:
Our choice for the project

No.4	Yellow taxis, green taxis, Uber and bikes
With the introduction of green taxis, Ubers and CitiBike, an interesting question is how these new modes of transportation have impacted urban movement in New York City.
Are previously underserved regions (e.g., Harlem) better served now by the green taxis?  Has Uber negatively affected the revenues for yellow taxi companies? Or is Uber catering to a different set of customers?
Are residents opting to use CitiBike instead of taxis/Uber?

Here are articles that discuss some of these issues:
- http://fivethirtyeight.com/tag/uber/
- http://www.cnbc.com/2015/11/17/new-york-city-sued-over-uber-by-taxi-owners-say-livelihood-under-threat.html

The data sets we will use

- 2015 Yellow Taxi Dataset
  	Available at http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml
 	Collect all the data files from 2015 (yellow taxi only)
Metadata available at: http://www.nyc.gov/html/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
  	Temporal data is in EST (second resolution).
  	Spatial data is in GPS.

	- 2015 Green Taxi Dataset
	Available at http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml
	Collect all the data files from 2015 (green taxi only)
Metadata available at: http://www.nyc.gov/html/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf
  	Temporal data is in EST (second resolution).
  	Spatial data is in GPS.
- Citi Bike Trip Histories
  	Available at: https://www.citibikenyc.com/system-data ("Citi Bike Trip Histories" section)
  	Collect all the data from 2015.
  	Temporal data is in EST (second resolution).
 	Spatial data is in GPS.

	- Uber Dataset
Available at:	http://toddwschneider.com/posts/analyzing-1-1-billion-nyc-taxi-and-uber-trips-with-a-vengeance/

 	- Weather Dataset
  Available at:http://www7.ncdc.noaa.gov/CDO/dataproduct
  Metadata available at:http://www7.ncdc.noaa.gov/CDO/GSOD_DESC.txt

- Income Dataset
	   Available at: https://www.incomebyzipcode.com/newyork

IRS tax return,estimated income,2013

https://www.irs.gov/uac/SOI-Tax-Stats-Individual-Income-Tax-Statistics-2013-ZIP-Code-Data-(SOI)

Census Data, which gives the ZCTA codes instead of zipcode. 
here is a paper explaining the difference of them.(http://blog.cubitplanning.com/2012/03/of-zip-codes-and-zctas/)

http://factfinder.census.gov/faces/nav/jsf/pages/download_center.xhtml#none

Zipcode polygon 

http://catalog.civicdashboards.com/dataset/11fd957a-8885-42ef-aa49-5c879ec93fac/resource/eec14f19-9794-46ef-9bf4-7f6835ffbf4c/download/a5305aa3500748a2b08a6925302f2eednyczipcodetabulationareas.geojson


The tasks we will carry out

What are people’s preference among these means of transportation under different weather circumstances? (201501)
Data key: date and site (one month),  yellow cab(A), green cab(T), citibike(done), uber(J)
2015-04-27
Features: rain, snow, sunny; Response: average of the number of trips / (distance) / (fare or tip) 
For rain: inches; Response: 
For snow:
For Sunny:




What are people’s preference among these means of transportation in difference average income zip code zone?
Data: key: zip code(calculate); yellow(); green(); citibike(); uber()


1. Has Uber negatively affected the revenues for yellow taxi companies?
http://www.thestreet.com/story/13367110/1/new-york-city-taxi-revenue-accelerates-decline-in-uber-era.html

2. Are residents opting to use CitiBike instead of taxis/Uber?

3. What are people’s preference among these means of transportation under different weather circumstances?

4*.

5. Are previously underserved regions (e.g. Harlem) better served now by the green taxis?
6. Is Uber catering to a different set customers?

A proposed timeline with weekly milestones

## April 17: 
Process all the datasets using Hadoop, including but not limited to clean, join and     calculation. 
Add a new section in our Google Doc entitled "Status Report" describing any issues you encountered and updates to your initial plan. 


Status Report
Issues：
Taxis data files are too large, yellow cabs has about 2GB data each month for 2015. Thus, we think we need to reorganize the data and group them by week or month instead of day. (Discussion with professor is needed.)
Need more specific steps to finish each task
Need determine the expected results
Need structure schema in order to make visualization better 
Loss of Income data. 25 dollars are needed to download the data. 
Loss of Uber data. Only half of the 2015 year uber data is available. Also this dataset contains only pickup location. Needs help and suggestion from the professor.


## April 24: 
Finish processing all the datasets and start analysis based on our tasks.
Status report
Datasets:
For each data of transportation:yellow cab(A), green cab(T), citibike(done), uber(J). join with weather. Key: date and site
Join with income data: key: zip code(calculate); yellow(); green(); citibike(); uber()

May 1: 
Continue analyzing data and start visualization using d3 based on completed task.  Add a new section in your Google Doc entitled "Status Report and Preliminary Results", describing your preliminary results and any updates. 

Status Report:
What are people’s preference among these means of transportation under different weather circumstances? (201501)
Task1: 
Input: merged data with yellow cab, green cab, citibike and weather
Output:  for rain, average of the number of trips
Map: {classify indicator of each weather conditions by FRSHTT, date}
Reduce: # of trips / # of date

Features: rain, snow, sunny Response: average of the number of trips / (distance) / (fare or tip) 
For rain: inches; Response: 
For snow:
For Sunny:


## May 8：
Finish analyze all the data and focus on d3 visualization.
Polishing for final report. 

## May 13th: 
Final project report due. Add a new section in your Google Doc entitled "Project Report"

## May 16th: 
Complete d3 visualization and get ready for the project presentation. Project presentation: each group will present a poster with their results. The instructors will select the best 3 presentations; students in the selected groups will get extra credit: one letter upgrade (e.g., if the final grade is a B, the student will get a B+)
