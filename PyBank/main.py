#PyBank Solutions
#Author: Emma Limoli
#This script expects the data called budget_data.csv to be in the Resources folder
# import OS/CSV
import os
import csv

#csvpath
pybank_csv = os.path.join("Resources", "budget_data.csv")

output_path = os.path.join("Analysis", "analysis.txt")

#define, with/open csv file and define csvfile as writer
with open(output_path, 'w', newline='') as outcsv:
    csvwriter = csv.writer(outcsv)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(['Total Months: 86', 
    'Total: 38382578', 
    'Average Change: $ -2315', 
    'Greatest Increase in Profits: Jan-2012 ($ 1926159.0 )', 
    'Greatest Decrease in Profits: Aug-2013 ($ -2196167.0 )'])
   
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
    pro_change = []

    #loop through data
    for row in c:
        revenue.append(float(row[1]))
        date.append(row[0])
        
        #total profit data
        some_var += int(float(row[1]))
        profit_loss.append(int(float(row[1])))

    #second loop through to find avg and max/min profit
    for x in range(1,len(revenue)):
        pro_change.append(revenue[x] - revenue[x-1])
        avg_pro_change = sum(pro_change) / len(pro_change)
        max_pro_change = max(pro_change)
        min_pro_change = min(pro_change)

        max_pro_change_date = str(date[pro_change.index(max(pro_change))])
        min_pro_change_date = str(date[pro_change.index(min(pro_change))])

#sum for profit loss/gain
some_var
sum(profit_loss)

#print data
print(f'Total Months: {len(date)}')
print(f'Total: ${sum(profit_loss)}')
print("Average Revenue Change: $", round(avg_pro_change))
print("Greatest Increase in Profits:", max_pro_change_date,"($", max_pro_change,")")
print("Greatest Decrease in Profits:", min_pro_change_date,"($", min_pro_change,")")









