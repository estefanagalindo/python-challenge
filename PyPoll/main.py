import os
import csv
# Bring in data from the csv file.
csvpath = "election_data.csv"
# add up votes by candidate
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # create lists for candidate
    Candidate = []
    candidateList = []
    totalVoters = 0
    # add to list
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
    # winner based on the highest number of votes.
    keyMax = max(votes, key=votes.get)
    print("Winner:  " + keyMax)
    print("-------------------------")

