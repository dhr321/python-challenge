# Script for PyBank assignment.
# Dave Rodriguez. david.h.rodriguez@gmail.com

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import os
import csv



# Initialize variables.
monthcount = 0
netpl = 0
avepl = 0
maxprofit = 0
maxloss = 0

# Lists to store data.
date = []
pl = []

# os.getcwd()

csvpath = os.path.join('Resources', 'budget_data.csv')

# Open .csv data file.
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header.
    # Create two lists: one for dates and one for profit/loss.
    # Count the rows in the .csv file to get count of months.
    for row in csvreader:
        #print(row[1])
        date.append(row[0])
        pl.append(row[1])
        monthcount = monthcount + 1

    for x in pl:
        #print(int(x))

        netpl = netpl + int(x)
        if int(x) > maxprofit:
            maxprofit = int(x)
        elif int(x) < maxloss:
            maxloss = int(x)



        #if profit > maxprofit:
         #   maxprofit = row[1]
        #   maxprofit_dt = row[0]


    avepl = round(netpl / monthcount,2)


    print()
    print("-------------------------------------")
    print("Total Months: " + str(monthcount))
    print("Total $" + str(netpl))
    print("Average Change: $ " + str(avepl))
    print("Greatest Increase in Profits: " + str(maxprofit))
    print("Greatest Dencrease in Profits: " + str(maxloss))
