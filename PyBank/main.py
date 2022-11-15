#import modules
import csv
import os

#setting path
budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv"))

#setting output
text_path = "output.txt"

#Setting variables
total_months = 0
total_profit = 0
revenue = []
previous_profit = 0
month_of_change = []
profit_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
profit_change_list = []
revenue_average = 0

#openning csv
with open(budget_data_csv, 'r') as csvfile:  
    csvreader = csv.DictReader(csvfile)

    #loops for total month
    for row in csvreader:

        #Counting months 
        total_months += 1 

        #Total_profit calculation
        total_profit = total_profit + int(row["Profit/Losses"])

        #Average_Change in profit calculation
        profit_change = float(row["Profit/Losses"])- previous_profit
        previous_profit = float(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change = [month_of_change] + [row["Date"]]

        #Greatest increase in profit
        if profit_change>greatest_increase[1]:
            greatest_increase[1]= profit_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in profit
        if profit_change<greatest_decrease[1]:
            greatest_decrease[1]= profit_change
            greatest_decrease[0] = row['Date']
    revenue_average = sum(profit_change_list)/len(profit_change_list)

#Print to Terminal
print("Financial Analysis\n")
print("---------------------\n")
print("Total Months: %d\n" % total_months)
print("Total Revenue: $%d\n" % total_profit)
print("Average Change: $%d\n" % revenue_average)
print("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
print("Greatest Decrease in Profits: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

#write changes to csv
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_profit)
    file.write("Average Change: $%d\n" % revenue_average)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
