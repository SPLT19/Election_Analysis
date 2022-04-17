# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
total_cvotes = 0
#2 Write down the names of all the candidates.
#Candidate options
candidate_options = []

# 3.1 Declare the empty dictionary for counting the votes on each candidate.
candidate_votes = {}

# Challenge 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}


#4.3 Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Challenge 2: Track the largest county and county voter turnout.
largest_county = ""
county_count = 0


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
        total_cvotes += 1

# 1.3 Print the total votes.
# print(total_votes)

#2 Write down the names of all the candidates. 
# Print the candidate name from each row.
        candidate_name = row[2]


# Challenge 3: Extract the county name from each row.
        county_name = row[1]


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

 # Challenge 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # Ch 4b: Add the existing county to the list of counties.
            county_options.append(county_name)


            # CH4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # CHallenge 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

#Print final vote count to the terminal
    election_results = (
    f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    #Save final vote count to text file.
    txt_file.write(election_results)


    # 3.2 Print the candidate vote dictionary.
    #print(candidate_votes)

 # Challenge 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        #CH 6b: Retrieve the county vote count.
        cvotes = county_votes[county_name]
        #CH 6c: Calculate the percentage of votes for the county.
        cvote_percentage = float(cvotes) / float(total_cvotes) * 100

         #CH 6d: Print the county results to the terminal.
        
        print(f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})")
    
        
         #CH 6e: Save the county votes to a text file.
        county_results = ( f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})") 

         #CH 6f: Write an if statement to determine the winning county and get its vote count.
        
        

    #Challenge 7: Print the county with the largest turnout to the terminal.
    

    #Challenge 8: Save the county with the largest turnout to a text file.

    


    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #4 Get the total votes for each candidate.
        #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
       
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #4.3 Winning Candidate and Winning Count Tracker
            # Determine winning vote count and candidate
            # 4.3.1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 4.3.2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
                # 4.3.3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
    print(winning_candidate_summary)

    #5 Get the total votes cast for the election.
    #print("The total votes cast for the elections were a total of " + str(total_votes) + " votes.") 


    #goals
    #A complete list of candidates who received votes
    #Total number of votes each candidate received
    #Percentage of votes each candidate won
    #The winner of the election based on popular vote

    # Close the file.
    #election_data.close()



