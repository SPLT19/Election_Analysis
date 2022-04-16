#import modules to read csv
#import csv
#dir(csv)

#Task Goals and sub goals
#Total number of votes cast

#1 Open the data file.
    #Full path Source from file "C:\Users\splt1\Election_Analysis\Resources\election_results.csv" 
    #file_variable = open(filename, mode)     
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')
#with open(file_to_load) as election_data:
# To do: perform analysis.
#    print(election_data)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

#2 Write down the names of all the candidates.
#3 Add a vote count for each candidate.
#4 Get the total votes for each candidate.
#5 Get the total votes cast for the election.


#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote


# Close the file.
#election_data.close()



