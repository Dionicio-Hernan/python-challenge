# Establish Import Statement
import os

# Module for reading files
import csv

# Establish path to file 
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        months = row[0]
        profit_loss = row[1]

# Extract total number of months in dataset
    for row in csvreader:
            months.append(row[0])

# Add profit and loss values
profit_loss.append(int(row[1]))

# Variables
total_number_months = len(months)
profit_loss_net_total = sum((profit_loss))
