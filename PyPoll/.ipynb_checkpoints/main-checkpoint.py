import os
import csv
# Import data from the csv file.
csvpath = "election_data.csv"
# Calculate votes by candidate
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Set up lists for candidate and candidatelist.
    Candidate = []
    candidateList = []
    totalVoters = 0
    # add that to a dictionary - votes
    votes = {}
  #  CandidateDict = {}

    # loop through the data
    for row in csvreader:
        Candidate = row[2]
        if Candidate not in candidateList:
            candidateList.append(Candidate)
            votes[Candidate] = 0
        votes[Candidate] += 1
        totalVoters += 1


# Print out the results for each candidate.
    print("Election Results")
    print("-------------------------")
    # Calculate the % of votes cast
    print("Total Votes: " + str('{:,.0f}'.format(totalVoters)))
    print("-------------------------")
    for i in votes:
        PctVotes = '{:,.3f}'.format((votes[i]/totalVoters)*100)
        print(i + ": " + str(PctVotes) +
              "% (" + str('{:,.0f}'.format(votes[i])) + ")")
    print("-------------------------")
    # Declare a winner based on the highest number of votes.
    keyMax = max(votes, key=votes.get)
    print("Winner:  " + keyMax)
    print("-------------------------")

