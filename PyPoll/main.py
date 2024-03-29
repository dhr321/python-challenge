# Script for PyPoll assignment.
# Dave Rodriguez. david.h.rodriguez@gmail.com

# Import dependencies
import os
import csv

# Initialize variables.
votecount = 0
votes = 0
leader = 0

# Lists to store data.
all_candidates = []
unique_candidates = []

csvpath = os.path.join('Resources', 'election_data.csv')

# Open .csv data file.
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header.
    # Populate a list of all the selected candidate's names
    # Count the total number of votes.
    for row in csvreader:
        all_candidates.append(row[2])
        votecount = votecount + 1

    # Find unique candidate names and add them to a new list.
    # Found syntax example here: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python/37163210
    for x in all_candidates:
        if x not in unique_candidates:
            unique_candidates.append(x)
    # print(unique_candidates)

    # Start printing results to terminal.
    print("\n--------------------------")
    print("Election Results")
    print("--------------------------")
    print("Total Votes: " + str(votecount))
    print("--------------------------")

    # Send output to a new text file and then close it.
    # Need to send output to screen and to text file as it is generated
    # instead of dumping it all at once.
    f = open("election_summary.txt", "w")
    f.write("--------------------------")
    f.write("\nElection Results")
    f.write("\n--------------------------")
    f.write("\nTotal Votes: " + str(votecount))
    f.write("\n--------------------------")

    # Loop through list of four candidates.
    for name in unique_candidates:
        #print(name)

        # Loop through list of all selected voter names.
        for votename in all_candidates:
            if votename == name:
                votes = votes + 1

        # Output the candidate's name and how many votes collected.
        print(name + ": " + str(round(votes/votecount*100,3)) + "% (" + str(votes) + ")")
        f.write("\n" + name + ": " + str(round(votes / votecount * 100, 3)) + "% (" + str(votes) + ")")

        # Identify the candidate with the most votes.
        if votes > leader:
            leader = votes
            winner = name
        votes = 0

    print("--------------------------")
    print("Winner: " + winner)
    print("--------------------------")

    f.write("\n--------------------------")
    f.write("\nWinner: " + winner)
    f.write("\n--------------------------")
    f.close()
