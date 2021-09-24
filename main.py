import csv
import pandas

#build a new dataframe
#Fur color and count

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

list_of_colors = data["Primary Fur Color"].to_list()

gray = 0
red = 0
black = 0

for color in list_of_colors:
    if color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        red += 1
    elif color == "Black":
        black += 1

print(gray)
print(red)
print(black)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

squirrel_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}

print(squirrel_dict)

squirrel_dataframe = pandas.DataFrame(squirrel_dict)

print(squirrel_dataframe)

squirrel_dataframe.to_csv("squirrel_count.csv")



# import csv
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))  #this is a DataFrame object from pandas library equivalent to a whole spreadsheet table.
#                     #has many methods that allow conversion to specific data files like html, json, etc.  also
#                     #data types like dictionary
#
# print(type(data["temp"])) #panda library Series object very similiar to a single column in a table.  behaves like a
#                             #list datatype
#
# print(data["temp"])
#
# #converts data object information to dictionary.  stores in data_dict variable as dictionary data type.
# data_dict = data.to_dict()
#
# #converts temp column data to list.  stores in temp_list variable as a list
# temp_list = data["temp"].to_list()
#
# average = data["temp"].sum() / len(temp_list)
#
# average_panda_method = data["temp"].mean()
#
# print(f"Average is: {average}")
#
# print(f"Average with panda method is: {average_panda_method}")
#
# maximum = data["temp"].max()
#
# print(f"Maximum is: {maximum}")
#
# #gets data from column named condition
# print(data["condition"])
#
# #can also use below code as well.  panda makes top row of columns into attributes
# #case sensitive.  key value pairs act like dictionary
# print(data.condition)
#
# #Get Data in Row
# print(data[data.day == "Monday"])
#
# #print(data.temp.max())
#
# #gets row with maximum temperature can use conditional operators.
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)  #digs into row named Monday and column named 'condition'
#
# #gets temperature from row named Monday.
# monday_temp = int(monday.temp)
#
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# #create a data frame from scratch:
#
# #creates dictionary
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# #formats dictionary into a DataFrame object.  stores it into object named data
# data = pandas.DataFrame(data_dict)
# print(data)
#
# #formats to csv.  then stores this information into a new file named new_data.csv
# data.to_csv("new_data.csv")
#
#
#
#
#
#
#
#
