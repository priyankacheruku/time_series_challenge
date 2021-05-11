##need to install python
# importing pandas library
import pandas as pd
from datetime import date as d, datetime as dt

# txt file to csv file
dataframe = pd.read_csv("time_series.txt", names=["serial no", "date", "time", "state"])

# storing this dataframe in a csv file
dataframe.to_csv('time_series.csv',index = None)

print("###########given data frame###########")
print(dataframe)


def process(date,time):
	# convert the string to datetime
	time_str = dt.strptime(time.strip(), "%I:%M %p")
	time = (dt.strftime(time_str,"%H:%M"))	
	date = tuple(int(i) for i in date.split(" ") if i.isdigit())
	time = tuple(int(i) for i in time.split(":") if i.isdigit())

	date = date+time
	# return datetime object
	return dt(*date)


# using list comprehension to process the data
dataframe["date_time"]= pd.Series([
    process(date,time)
    for (date, time) in zip(dataframe['date'], dataframe['time'])
  ])
  

## after processing the data into datetime format
print("###########processed###########")
print(dataframe)

#applying aggregation using unique time series
aggregation_functions = {'date_time': 'diff'}
dataframe["difference"] = dataframe.groupby(dataframe['serial no']).aggregate(aggregation_functions)

print("###########Difference between start and stop  ###########")
print(dataframe)

print("###average of start and stop")
print(dataframe["difference"].mean())
