# Import the os module
# This will allow to create file path across operating system
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv') 

#Variables
number_months = 0
net_profit_loss = 0
greatest_increase = 0
greatest_decrease = 0
#Open and read using csv module
with open(csvpath, newline='') as csvfile:
    #Csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(csvreader)
    #print(f"CSV Header: {csv_header}")
    #Read each row of the file after the header
    for row in csvreader:           
        #print(row)
        #Calculates the number of months included in the dataset
        number_months = number_months + 1
        #Calculates the net total amount of "Profit/Losses" over the entire period
        profit_loss = int(row[1])
        net_profit_loss = net_profit_loss + profit_loss
        if (profit_loss > greatest_increase):
            greatest_increase = profit_loss
        elif (profit_loss < greatest_decrease):
            greatest_decrease = profit_loss

    print(f'Total Months: {number_months}')
    print(f'Total Net Profit and Loss: {net_profit_loss}')
    print(f'Greatest Increase in Profits: {greatest_increase}')
    print(f'Greatest Decrease in Profits: {greatest_decrease}')

   