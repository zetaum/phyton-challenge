#HW 3 - PyPoll
# Import the os module
# This will allow to create file path across operating system
import os
# Module for reading csv files
import csv
#Set the path for the csv file
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv') 

#Variables
total_votes = 0
khan_votes = 0
li_votes = 0
correy_votes = 0
otooley_votes = 0



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


    #Read each row after the header
    for row in csvreader:
        #Calculates the number of votes cast included in the dataset
        total_votes = total_votes + 1

        #Calculates the number of votes for each candidate
        if(row[2] == 'Khan'):
            khan_votes = khan_votes + 1
        elif(row[2] == 'Correy'):
            correy_votes = correy_votes + 1
        elif(row[2] == 'Li'):
            li_votes = li_votes + 1
        else:
            otooley_votes = otooley_votes + 1
        
        #Calculates the percentage of votes each candidate won
        khan_percentage = khan_votes / total_votes
        correy_percentage = correy_votes / total_votes
        li_percentage = li_votes / total_votes
        otooley_percentage = otooley_votes / total_votes

        #Calculates the winner of the elction based on popular vote
        winner = max(khan_votes, correy_votes, li_votes, otooley_votes)
        if winner == khan_votes:
            election_winner = "Khan"
        elif winner == correy_votes:
            election_winner = "Correy"
        elif winner == li_votes:
            election_winner = "Li"
        else:
            election_winner = "O'Tooley"




#Print analysis
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'-------------------------')
    print(f'Khan: {khan_percentage:.3%} ({khan_votes})')
    print(f'Correy: {correy_percentage:.3%} ({correy_votes})')
    print(f'Li: {li_percentage:.3%} ({li_votes})')
    print(f'OTooley: {otooley_percentage:.3%} ({otooley_votes})')
    print(f'-------------------------')
    print(f'Winner: {election_winner}')
    print(f'-------------------------')

#Set the path for the final election results script to be exported
    output_file = os.path.join('PyPoll', 'Resources', 'election_data.txt')
    #Open and read file using "write" module
with open(output_file, 'w') as text:
    # Write election results to a new text file
    text.write(f'Election Results\n')
    text.write(f'-------------------------\n')
    text.write(f'Total Votes: {total_votes}\n')
    text.write(f'Khan: {khan_percentage:.3%} ({khan_votes})\n')
    text.write(f'Correy: {correy_percentage:.3%} ({correy_votes})\n')
    text.write(f'Li: {li_percentage:.3%} ({li_votes})\n')
    text.write(f'OTooley: {otooley_percentage:.3%} ({otooley_votes})\n')
    text.write(f'-------------------------\n')
    text.write(f'Winner: {election_winner}\n')
    text.write(f'-------------------------\n')