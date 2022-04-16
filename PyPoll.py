# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#2 Write down the names of all the candidates.
#Candidate options
candidate_options = []

# 3.1 Declare the empty dictionary for counting the votes on each candidate.
candidate_votes = {}

#1.1 Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
   # test walktrhouh: print(headers) test

 # Print each row in the CSV file.
    for row in file_reader:
        # 1.2 Add to the total vote count.
        total_votes += 1

# 1.3 Print the total votes.
# print(total_votes)

#2 Write down the names of all the candidates. 
# Print the candidate name from each row.
        candidate_name = row[2]

  # 2.1 v2 If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)       

# 2.1 Add the candidate name to the candidate list.
        #candidate_options.append(candidate_name)

 #3.1.2 Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            
#2.2 Print the candidate list.
#print(candidate_options)

#3.3.2 Add a vote count for each candidate.
            #3.3.1 candidate_votes[candidate_name] += 1
        candidate_votes[candidate_name] += 1
# 3.2 Print the candidate vote dictionary.
#print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")





#4 Get the total votes for each candidate.
#5 Get the total votes cast for the election.



#goals
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote


# Close the file.
#election_data.close()



