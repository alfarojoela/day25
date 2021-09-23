import csv
import pandas

#other format:
#   data_file = open("weather_data.csv")
#   data = data_file.readlines()
#   data_file.close()



# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
temp_list = data["temp"].to_list()

average = sum(temp_list) / len(temp_list)

print(data["temp"].mean())

print(data["temp"].max())

#get data in columns
print(data["condition"])
print(data.condition)

#get data in row
#data[data["day"]]

data[data.day == "Monday"]

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)




