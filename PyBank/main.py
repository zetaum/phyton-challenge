# Import the os module
# This will allow to create file path across operating system
import os
# Module for reading csv files
import csv
#Set the path for the csv file
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv') 

#Variables
number_months = 0
net_profit_loss = 0
greatest_increase = 0
greatest_increase_date = 0
greatest_decrease = 0
greatest_decrease_date = 0
previous_result = 0
monthly_change = []
count_month = []

#Open and read using csv module
with open(csvpath, newline='') as csvfile:
    #Csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(csvreader)
    #print(f"CSV Header: {csv_header}")
    #Read each row of the file after the header
    row = next(csvreader)



    previous_result = int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_date = row[0]
    greatest_decrease = int(row[1])
    number_months = number_months + 1
    profit_loss = int(row[1])
    net_profit_loss = net_profit_loss + profit_loss
    

 
    for row in csvreader:           
        #print(row)
        #Calculates the number of months included in the dataset
        number_months = number_months + 1
        #Calculates the net total amount of "Profit/Losses" over the entire period
        profit_loss = int(row[1])
        net_profit_loss = net_profit_loss + profit_loss
       

        #Calculate change in "Profit/Losses" between current month and previous month
        change_result = int(row[1]) - previous_result
        previous_result = int(row[1])
        monthly_change.append(change_result)
        count_month.append(row[0])

        #Calculate the average of the changes in "Profit/Losses" over the entire period
        change_average = sum(monthly_change)/len(monthly_change)
        highest = max(monthly_change)
        lowest  = min(monthly_change)


        #Calculate greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_date = row[0]
        
        
        #Calculate greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_date = row[0]

    print(f'Total Months: {number_months}')
    print(f'Total Net Profit and Loss: {net_profit_loss}')
    print(f'Total Average Change: ${change_average:.2f}')
    print(f'Greatest Increase in Profits: (${greatest_increase})')
    print(f'Greatest Increase in Profits- Date : {greatest_increase_date}')
    print(f'Greatest Decrease in Profits: (${greatest_decrease})')
    print(f'Greatest Decrease in Profits- Date : {greatest_decrease_date}')
   