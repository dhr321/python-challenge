# Script for PyBank assignment.
# Dave Rodriguez. david.h.rodriguez@gmail.com

# Import dependencies
import os
import csv


# Initialize variables.
monthcount = 0
thisMonthProfit = 0
lastMonthProfit = 0
netpl = 0 # net profit or loss
sumChange = 0 # sum of all month-to-month changes
maxPosChange = 0
maxNegChange = 0

# Lists to store data.
date = []
pl = []
change = []

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

        # Populate a list of the calculated month-to-month changes.
        thisMonthProfit = int(x)
        change.append(int(x) - lastMonthProfit)

        # After calculation complete, move value of current month to last month.
        lastMonthProfit = thisMonthProfit
    # print(change)

    # Loop through the list of calculated changes.
    # Calculate average monthly change.
    # Identify maximum positive and negative changes.
    for x in change:
        sumChange = sumChange + int(x)
        if x > maxPosChange:
            maxPosChange = x
        elif x < maxNegChange:
            maxNegChange = x

    # Calculate the average monthly change.
    # Subtract the first calculated change from the sum because it's not really a "change".
    # Also, subtract 1 from the monthcount because the number of monthly changes
    # is one less than the number of months.
    aveChange = round((sumChange - change[0]) / (monthcount-1),2)


    # Find dates of max positive and negative changes.
    # The index of the values in the list of changes should
    # correspond to the index in the list of dates.
    maxPosChange_index = change.index(maxPosChange)
    maxPosChange_date = date[maxPosChange_index]

    maxNegChange_index = change.index(maxNegChange)
    maxNegChange_date = date[maxNegChange_index]

    print()
    print("Financial Analysis")
    print("-------------------------------------")
    print("Total Months: " + str(monthcount))
    print("Total $" + str(netpl))
    print("Average Change: $" + str(aveChange))
    print("Greatest Increase in Profits: " + maxPosChange_date + " ($" + str(maxPosChange) + ")")
    print("Greatest Decrease in Profits: " + maxNegChange_date + " ($" + str(maxNegChange) + ")")

# Send output to a new text file and then close it.
f = open("budget_summary.txt", "w")
# f.write("\n ")
f.write("Financial Analysis")
f.write("\n-------------------------------------")
f.write("\nTotal Months: " + str(monthcount))
f.write("\nTotal $" + str(netpl))
f.write("\nAverage Change: $" + str(aveChange))
f.write("\nGreatest Increase in Profits: " + maxPosChange_date + " ($" + str(maxPosChange) + ")")
f.write("\nGreatest Decrease in Profits: " + maxNegChange_date + " ($" + str(maxNegChange) + ")")
f.close()