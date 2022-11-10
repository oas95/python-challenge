#import modules
import csv
import os

#setting path
election_data_csv = os.path.join("C:\\Users\\gbnlo\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#setting variables
total_votes = 0 
charles_votes = 0 
diana_votes = 0 
raymon_votes = 0

#openning csv
with open(election_data_csv, 'r') as csvfile:  
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:

        #counting votes for each unique candidate and storing  
        total_votes +=1 
        
        if row[2] == "Charles Casper Stockham":
            charles_votes +=1
        elif row[2] == "Diana DeGette":
            diana_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes +=1

#finding winner
#creating dictionary
candidates = ["Charles", "Diana", "Raymon"]
votes = [charles_votes, diana_votes, raymon_votes]

#Winner
dict_cand_and_votes = dict(zip(candidates,votes))   
winner = max(dict_cand_and_votes, winner=dict_cand_and_votes)

#percentage calculation
charles_percent = (charles_votes/total_votes)*100
diana_percent = (diana_votes/total_votes)*100
raymon_percent = (raymon_votes/total_votes)*100


#printing table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")