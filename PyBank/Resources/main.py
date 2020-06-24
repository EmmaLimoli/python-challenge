# import OS/CSV
import os
import csv

#csvpath
pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

#define function and use pybank_data as parameter
#def financial_analysis(record_data):

#define variables 
    #time = int(record_data[0])
    #profit_loss = int(record_data[1])
    #total = 0
    

#define equations


    #net_amount =
    #average_change = 
    #increase = 
    #decrease =

#if/else statements 
#pull total number of months in data
#pull net total amount of profit/loss over entire period
#pull average of the changes in profit/loss
#greatest increase in profits(date and amount) over entire period
#greatest decrease in losses (date and amount) over entire period
#print statements
#with open
with open(pybank_csv, 'r') as csvfile:
        c = csv.reader(csvfile, delimiter=",")
        headers = next(c, None)
        data_group = input("Press Enter for financial analysis breakdown")
        some_var = 0
        some_list = []
        for r in c:
            some_var += int(float(r[1]))
            some_list.append(int(float(r[1])))
some_var
sum(some_list)
print(f'Total: ${sum(some_list)}')



        
        
        
        
        
        #csvreader = csv.reader(csvfile, delimiter=",")
        #header = next(csvreader)
        #

        #for row in csvreader:
            #if data_group == row[0]:
                #print(row[0])




            

#save as txt file
