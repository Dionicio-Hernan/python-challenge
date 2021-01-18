# Establish Import Statement
import os

# Module for reading files
import csv

# Establish variables
total_number_votes = 0
candidate_list = []
percentage_votes = 0
total_votes = 0
election_winner = 0 

# Establish path to file 
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
# Read header row first
    csv_header = next(csvreader)

# Total votes and cadidate list
for row in csvreader:
    total_number_votes += 1
    candidate = row [0]
    if candidate in candidates_list.keys():
        candidates_list[candidate] += 1
        else:
            candidate_list[candidate] =1

# Total votes
for row in csvreader:
    total_number_votes += 1
    y = candidate_list.count(x)
    total_number_votes.append(y)

# Insert candidate names into candidatelist
candidate_list.append(row[2])

# Get candidate names
for x in set(candidates):
    unique_id.append(x)

# percent of total votes per candidate
    percentage_votes = round(int(total_votes) / int(candidate_list), 2)
    review_percent.append(percent)

# Identify winner
election_winner = max(candidate_list)

# Print outputs
print("Total votes:" + total_number_votes)
print(candidate_list)
print(percentage_votes)
print(total_number_votes)
print(election_winner)





