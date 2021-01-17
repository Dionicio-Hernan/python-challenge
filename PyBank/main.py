# Establish Import Statement
import os

# Module for reading files
import csv

# Establish variables
total_months = 0
current _pl = 0 
previous_pl = 0
net_pl = 0 
total_change_pl = 0 
current_change_pl = 0
average_change_pl = 0 
biggest_increase = 0
biggest_decrease = 0 

# Establish path to file 
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    print(csv_reader)
    
# Read header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Read each row of data after the header
    for row in csvreader:
        print(row[0])

# Get total number of months from this file
total_months = row(0)

# Calculate net total amount in profit/loss
highs = []
high = int(row [1])
highs.append(high)

# Changes in Profit Loss over time, find average of changes

# Print outputs
print (total_months)
print (net_profit_loss) 
print (highs)
