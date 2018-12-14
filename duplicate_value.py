#Read the variables from the CSV
import csv

file = csv.reader(open('santa.csv'))

# Create the empty array to place the values into
chronal_array = []

# iterate over the file to place the values into the array
for row in file:
  chronal_array += row
  
  #convert the values from a str to int
  
chronal_array = list(map(int, chronal_array))
running_total = 0 
# generate a cumulative total array
cumulative_total = []
for i in chronal_array:
   running_total += i
   cumulative_total += [running_total] 
   if i in cumulative_total:
       print(i)
    