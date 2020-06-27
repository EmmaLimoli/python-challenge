# import OS/CSV
import os
import csv

#csvpath
pypoll_csv = os.path.join("..", "Resources", "election_data.csv")


#output csv path
#output_path = os.path.join("Analysis", "analysis2.txt")

#define with/open as writer

#define with/open as reader
with open(pypoll_csv, newline='') as csvfile:
    c = csv.reader(csvfile, delimiter=",")
    headers = next(c, None)
    
    #provide input
    data_group = input("Press Enter for voter data")
    
    #define variables
    total_votes = 0

    #vote_dict = {"1": "Khan",
    #Khan = True
    #Correy = True
    #Li = True
    #OTooley = True


#print({1})
#print


    #loop the data
    for row in c:
        total_votes += 1

    
#def mean(numbers):
    #row = [0]
    #date = []
    #total_votes = str(r)
    #rows = len(total_votes)
    #return float(sum(numbers)) / len(numbers)



#loop through data

#print data
print(f'Total Votes: {(total_votes)}')
#print(f'Total Votes: {sum([1,5,4,3])}')