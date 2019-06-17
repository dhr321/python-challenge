# Script for PyBank assignment.
# Dave Rodriguez. david.h.rodriguez@gmail.com

# Import dependencies
import os
import csv
import numpy as np


# Initialize variables.
votecount = 0
votes = 0

# Lists to store data.
voters = []
all_candidates = []
unique_candidates = []


# os.getcwd()

csvpath = os.path.join('Resources', 'election_data.csv')

# Open .csv data file.
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header.
    # Populate a list of all the selected candidate names
    for row in csvreader:
        all_candidates.append(row[2])
        votecount = votecount + 1

    # Find unique candidate names and add them to a new list.
    # Found syntax example here: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python/37163210
    for x in all_candidates:
        if x not in unique_candidates:
            unique_candidates.append(x)
    # print(unique_candidates)

    print("\n--------------------------")
    print("Election Results")
    print("--------------------------")
    print("Total Votes: " + str(votecount))
    print("--------------------------")

    for name in unique_candidates:
        #print(name)
        for votename in all_candidates:
            if votename == name:
                votes = votes + 1
        print(name + ": " + str(round(votes/votecount*100,3)) + "% (" + str(votes) + ")")
        votes = 0



