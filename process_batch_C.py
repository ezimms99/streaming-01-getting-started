"""
Batch Process - third transformation

Reads from a file, transform, write to a new file.

In this case, covert degree K to degree F.

"""

import csv

input_file_name = "batchfile_2_kelvin.csv"
output_file_name = "batchfile_3_farenheit.csv"

input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w", newline='')

reader = csv.reader(input_file, delimiter=",")
writer = csv.writer(output_file, delimiter=",")

header = next(reader)
header_list = ["Year","Month","Day","Time","TempF"]
writer.writerow(header_list)

#This code takes the Kelvin Temperature and converts it to Farenheit
#The next lines writes the code to the new file with TempF included
for row in reader:
    Year, Month, Day, Time, TempK = row
    TempF = round((float(TempK) - 273.15) * 1.8 + 32.0,2)
    writer.writerow([Year, Month, Day, Time, TempF])

output_file.close()
input_file.close()