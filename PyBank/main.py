#import modules
import os
import csv

#set path for file
budget_data_csv = os.path.join("C:\\Users\\gbnlo\\python-challenge\\PyBank\\Resources\\budget_data.csv")

#set the output of the text file
text_path = "output.txt"

#Set variables
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
