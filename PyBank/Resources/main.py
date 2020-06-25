# import OS/CSV
import os
import csv

#csvpath
pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

#define, with/open csv file and define csvfile as reader
with open(pybank_csv, newline='') as csvfile:
    c = csv.reader(csvfile, delimiter=",")
    headers = next(c, None)
    
    #provide input
    data_group = input("Press Enter for financial analysis breakdown")
    
    #define variables 
    some_var = 0
    profit_loss = []
    row = [0]
    total_months = str(row[0])
    rows = len(total_months)
    revenue = []
    date = []
    rev_change = []

    #loop through data
    for row in c:
        revenue.append(float(row[1]))
        date.append(row[0])
        
        #total profit data
        some_var += int(float(row[1]))
        profit_loss.append(int(float(row[1])))

    #second loop through to find avg and max/min profit
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = sum(rev_change) / len(rev_change)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])

#sum for profit loss/gain
some_var
sum(profit_loss)

#print data
print(f'Total Months: {len(date)}')
print(f'Total: ${sum(profit_loss)}')
print("Average Revenue Change: $", round(avg_rev_change))
print("Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")






