# Script for PyBank assignment.
# Dave Rodriguez. david.h.rodriguez@gmail.com

# Import dependencies
import os
import csv


# Initialize variables.
monthcount = 0
netpl = 0 # net profit or loss
avepl = 0 # average profit or loss
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

    # Loop through new list of profit & loss numbers
    for x in pl:

        # Sum up the net profits and losses.
        netpl = netpl + int(x)

        # Test for conditions of greatest monthly profit and
        # greatest monthly loss.
        if int(x) > maxprofit:
            maxprofit = int(x)
        elif int(x) < maxloss:
            maxloss = int(x)

    # Calculate average monthly change.
    avepl = round(netpl / monthcount,2)

    # Find dates of max profit and max loss.
    maxprofit_index = pl.index(str(maxprofit))
    maxprofit_date = date[maxprofit_index]

    maxloss_index = pl.index(str(maxloss))
    maxloss_date = date[maxloss_index]

    print()
    print("-------------------------------------")
    print("Total Months: " + str(monthcount))
    print("Total $" + str(netpl))
    print("Average Change: $" + str(avepl))
    print("Greatest Increase in Profits: " + maxprofit_date + " " + str(maxprofit))
    print("Greatest Decrease in Profits: " + maxloss_date + " " + str(maxloss))

# Send output to a new text file and then close it.
f = open("budget_summary.txt", "w")
# f.write("\n ")
f.write("-------------------------------------")
f.write("\nTotal Months: " + str(monthcount))
f.write("\nTotal $" + str(netpl))
f.write("\nAverage Change: $" + str(avepl))
f.write("\nGreatest Increase in Profits: " + maxprofit_date + " " + str(maxprofit))
f.write("\nGreatest Decrease in Profits: " + maxloss_date + " " + str(maxloss))
f.close()