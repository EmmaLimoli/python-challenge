# import OS/CSV
import os
import csv

#csvpath
pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

#define function and use pybank_data as parameter
#def financial_analysis(record_data):
with open(pybank_csv, newline='') as csvfile:
    c = csv.reader(csvfile, delimiter=",")
    headers = next(c, None)
    data_group = input("Press Enter for financial analysis breakdown")
    some_var = 0

    #total months 
    profit_loss = []
    row = [0]
    total_months = str(row[0])
    rows = len(total_months)
    revenue = []
    date = []
    rev_change = []
    #total average of profit/loss
   

    #loop through data
    for row in c:
        revenue.append(float(row[1]))
        date.append(row[0])
        

        #average = int(row[1])
        #if average > 0:
            #print(average)
        #elif average < 0:
            #print(average)

    
 
        #total profit data
        some_var += int(float(row[1]))
        profit_loss.append(int(float(row[1])))
            
some_var
sum(profit_loss)
#sum(total_months)
print(f'Total Months: {len(date)}')
print(f'Total: ${sum(profit_loss)}')
print("Greatest Increase In Profits:", len(date))
print("Total Revenue: $", sum(revenue))

#print greatest increase in profits
#print greatest decrease in profits



print 




