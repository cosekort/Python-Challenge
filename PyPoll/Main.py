#import csv
import os
import csv 

#read file
csvfile=os.path.join('Resources', 'election_data.csv')

#initialize variables
Total_votes= 0
Ballot=0 
Canditate= 0
Canditate_votes= {}

#read csv
with open('Resources//election_data.csv', 'r') as file:
    csvreader=csv.reader(file, delimiter=",")
    next(csvreader)
    for row in csvreader:
        Ballot= row[0]
        County= row[1]
        Canditate= row[2]
        #print(Ballot)
        
        #Calculate Total Votes
        Total_votes= Total_votes +1
        #print(f"Total_votes: {Total_votes}")
        
        #Calculate Votes per canditate
        candidate= row[2]
        if candidate in Canditate_votes:
            Canditate_votes[candidate]+= 1
        else: 
            Canditate_votes[candidate]= 1
print("Election Results")   
print("----------------------")    
print(f"Total_votes: {Total_votes}")
print("----------------------") 

 
#Calculate Percentages for Canditate Votes
for candidate, votes in Canditate_votes.items():
        percentage = (votes / Total_votes) * 100
        print(f"{candidate}: {percentage:.2f}% ({votes} votes)")


#Find Winner 

#print(Canditate_votes)
Winner= max(Canditate_votes, key=Canditate_votes.get)
print("----------------------")  
print(f"Winner: {Winner}")

#Print ELection Results to .txt        
newfilepath = os.path.join("..\\Analysis\\Pypoll.txt")
with open("Analysis\\Pypoll.txt", "w") as file:
    print("Election Results", file=file)   
    print("----------------------", file=file)    
    print(f"Total_votes: {Total_votes}", file=file)
    print("----------------------", file=file)
    print(f"{candidate}: {percentage:.2f}% ({votes} votes)", file=file)
    print("----------------------", file=file)   
    print(f"Winner: {Winner}", file=file)
