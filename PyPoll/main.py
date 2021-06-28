
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

# A counter for the total number of votes
total = 0
## A list to capture the names of candidate
candidates = []
# A list to capture the number of votes each candidate receives
Total_votes = []
# A list to capture the percentage of total votes each candidate garners
percentagevotes = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
#     To skip the header
    next(csvreader)

    for row in csvreader:
        # Add to our vote-counter 
        total += 1 
        
        #append the candidates to the candidates list
        #find the index value of each candidate in the candidate list
        #append their vote values by 1 each time they are found to increase their vote count
        if row[2] not in candidates:
            candidates.append(row[2])
            Total_votes.append(1)
        else:
            index = candidates.index(row[2])
            Total_votes[index] += 1
            
    # Add to percent_votes list
    for votes in Total_votes:
        percentage = ((votes / total) * 100)
        percentagevotes.append("%.3f%%" % percentage)
        
    #To find the maximum votes recieved by the winner candidate
    maximumvotes = max(Total_votes,key=lambda x:float(x))
    
    #To find the winner
    tofindwinner = {candidates[i]: Total_votes[i] for i in range(len(candidates))}
    
    #Winner announced 
    def get_key_from_value(tofindwinner, winner):
        keys = [k for k, v in tofindwinner.items() if v == maximumvotes]
        if keys:
            return keys[0]
        return None
    Winner = get_key_from_value(tofindwinner, 'winner')
    
    #Printing all the required results 
    print("Election Results")
    print("------------------------") 
    print(f"Total Votes: {total}")
    print("------------------------")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {percentagevotes[i]} ({Total_votes[i]})")
    print("------------------------") 
    print (f"Winner: {Winner}")
    print("------------------------")
    
    #extracting an output text file with the results 
    outfile = open ("output.txt", "w")
    outfile.write ("Election Results \n")
    outfile.write ("------------------------\n")
    outfile.write (f"Total Votes: {total}\n")
    outfile.write ("------------------------\n")
    for i in range(len(candidates)):
        outfile.write (f"{candidates[i]}: {percentagevotes[i]} ({Total_votes[i]})\n")
    outfile.write ("------------------------\n")
    outfile.write (f"Winner: {Winner}\n")
    outfile.write ("------------------------\n")
    outfile.close()
    
    