import csv
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))  #this is a DataFrame object from pandas library equivalent to a whole spreadsheet table.
                    #has many methods that allow conversion to specific data files like html, json, etc.

print(type(data["temp"])) #panda library Series object very similiar to a single column in a table.  behaves like a
                            #list datatype

print(data["temp"])




