# Establish Import Statement
import os

# Module for reading files
import csv

# Establish variables
total_months = []
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

    print(csvreader)
    
# Read header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Read each row of data after the header
    for row in csvreader:

    # Get total number of months from this file
        total_months = len(set(row[0]))

    # Calculate net total amount in profit/loss
        current_pl = int(row[1])
        net_pl += current_pl

# Changes in Profit Loss over time, find average of changes
previous_pl = current_pl
next
else:
    current_change_pl = current_pl - previous_pl
    total_change_pl += current_change_pl
    previous_pl = current_pl

# Biggest increase in profits
if current_change_pl > max_increase:
    biggest_increase = current_change_pl
    biggest_decrease = row(0)

# Biggest decrease in profits
elif current_change_pl < biggest_decrease
biggest_decrease = current_change_pl
biggest_decrease_month = row (0)

# Average change in profit and loss
avg_change_pl = total_change_pl/total_months

# Print outputs
print ("Total months:" + total_months)
print (net_pl) 
