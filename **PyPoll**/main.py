# import modules
import os
import csv

# set path for file
csvpath = os.path.join("..","**PyPoll**", "election_data.csv")

# open csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # total number of votes cast
    for row in csvreader:
        print(row)
        votes = 0
    
        
  
 # open csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    # for loop including header
    total_votes = 0
    for row in csvreader:
        total_votes= total_votes+1
    total_votes = total_votes-1
print(total_votes)

# list of candidates who recieved votes
# votes per person
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    unique_list = []
    votes_pp = {} 
    
    next(csvreader, None)
    for row in csvreader:
        col=row[2]
        
        
            # check if exists in unique_list or not 
        if col not in unique_list: 
            unique_list.append(col)
            votes_pp[col]=0
        votes_pp[col]+=1

            
  
print(unique_list)
print(votes_pp)
    
        

# percentage of votes - make for loop to go through dictionary and divide by total to find percent of votes (for candidate in unique list)
winner = ""
highest_votes = 0
for candidate in unique_list:
    percent = (round((votes_pp.get(candidate)/total_votes)*100))
    if votes_pp.get(candidate) > highest_votes:
        winner = candidate
        highest_votes = votes_pp.get(candidate)
    
    
    print(candidate + ":" + str(percent))
#print(winner)


#Election results

output = (
f"Election Results\n"
f"------------------\n"
f"Total Votes {total_votes}\n"
f"------------------")

for candidate in unique_list:
    percent = (round((votes_pp.get(candidate)/total_votes)*100))
    
    output= output + candidate + ":" + str(percent) +"\n"
output= output + f"------------------\n"
output= output + f"winner: {winner}\n"

print(output)

# TODO: make into text file, change info to pypoll
with open("./analysis/analysis.txt","w") as textfile:
    textfile.write(output)