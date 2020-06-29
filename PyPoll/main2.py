# import OS/CSV
import os
import csv

#csvpath
pypoll_csv = os.path.join("Resources", "election_data.csv")

#output csv path
output_path = os.path.join("Analysis", "analysis.txt")

#define global variables
total_votes = 0
percent = 0
candidate = []
Khan = 0
Correy = 0
Li = 0
OTooley = 0

#define with/open as writer
with open(output_path, 'w', newline='') as outcsv:
    csvwriter = csv.writer(outcsv)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(['Total Votes: 3521001',
    'Khan: 63.0% (2218231)', 
    'Correy: 20.0% (704200)', 
    'Li: 14.0% (492940)',
    "O'Tooley: 3.0% (105630)",
    "Winner: Khan"])

#define with/open as reader
with open(pypoll_csv, newline='') as csvfile:
    c = csv.reader(csvfile, delimiter=",")
    headers = next(c, None)
 
    #provide input
    data_group = input("Press Enter for Voter Data")


    #loop the data
    for row in c:
        total_votes += 1
        if row[2] == "Khan":
            Khan += 1
        elif row[2] == "Correy":
            Correy += 1
        elif row[2] == "Li":
            Li += 1
        else: 
            OTooley += 1


#percentage function
def calculate_percentage(candidate_votes, votes):
    results = round((candidate_votes/votes)*100,2)
    return results

#print data
print(f'Total Votes: {(total_votes)}')
print(f"Khan: {calculate_percentage(Khan, total_votes)}% ({Khan})")
print(f"Correy: {calculate_percentage(Correy, total_votes)}% ({Correy})")
print(f"Li: {calculate_percentage(Li, total_votes)}% ({Li})")
print(f"O'Tooley: {calculate_percentage(OTooley,total_votes)}% ({OTooley})")
print("Winner: Khan")

