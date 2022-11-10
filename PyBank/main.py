#import modules
import os
import csv

#set path for file
budget_data_csv = os.path.join("C:\\Users\\gbnlo\\python-challenge\\PyBank\\Resources\\budget_data.csv")

#setting output
text_path = "output.txt"

#Setting  variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0

#openning csv
with open(budget_data_csv, 'r') as csvfile:  
    csvreader = csv.DictReader(csvfile)

    #loops for total month
    for row in csvreader:

        #Counting months 
        total_months += 1 

        #Total_revenue calculation
        total_revenue = total_revenue + int(row["Profit/Losses"])

        #Average_Change in revenue calculation
        revenue_change = float(row["Profit/Losess"]) - previous_revenue
        previous_revenue = float(row["Profit/Losess"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row['Date']]

        #Greatest increase in revenue 
        
