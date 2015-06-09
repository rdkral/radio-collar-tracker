//Parse.py

//Python code for parsing
//Keep csv file in same directory as python

//Import the python module
import csv

//open the csv file
f = open('/piksi_firmware/piksi_console/scripts/piksi_tools/console/position_log_20150507-121155.csv'))


//The CSV file looks like it gets saved in this format
//position_log_YEARMONTHDAY-HOURMINUTESECOND.csv

//read the file
csv_f = csv.reader(f)

//instantiate variables
time_list = []
longitude_list = []
latitude_list = []
altitude_list = []

//loop the rows and save them
for rows in csv_f:
	time_list.append(row[0])
	longitude_list.append(row[1])
	latitude_list.append(row[2])
	altitude_list.append(row[3])



//close the csv file
f.close()

//Print them
print time_list
print longitude_list
print latitude_list
print altitude_list