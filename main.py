import os
import csv

infile= os.path.join("election_data.csv")



with open(infile) as in_file:
    reader= csv.reader(in_file)

    header=next(reader)

    for row in reader:
        print(row)















# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------