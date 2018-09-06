#Import addins

import os
import csv
import pandas as pd
import numpy as np

#path for CSV file
csvpath = ("budget_data.csv")
#Read CSV into Panadas and give it a variable name Bank_pd
Bank_pd = pd.read_csv(csvpath, parse_dates=True)

#Number of month records in the CSV
Months = Bank_pd["Date"].count()

#Total amount of money captured in the data converted to currency
Total_Funds = '${:.0f}'.format(Bank_pd["Profit/Losses"].sum())

#Determine the amount of increase or decrease from the previous month
AmtChange = Bank_pd["Profit/Losses"].diff()
Bank_pd["Amount Changed"] = AmtChange

#Identify the greatest positive change
GreatestIncrease = '${:.0f}'.format(Bank_pd["Amount Changed"].max())
Gi_Date = (Bank_pd.loc[Bank_pd['Amount Changed'].idxmax(), 'Date'])

#Identify the greatest negative change
GreatestDecrease =  '${:.0f}'.format(Bank_pd["Amount Changed"].min())
Gd_Date =(Bank_pd.loc[Bank_pd['Amount Changed'].idxmin(), 'Date'])

#Find the average change
Average = '${:.2f}'.format(Bank_pd['Amount Changed'].mean())

#PRINTING BELOW
print("Financial Analysis")
print("-"*25)
print(f"Total Months: {Months}")
print(f"Total: {Total_Funds}")
print(f"Average Change:  {Average}")
print(f"Greatest Increase in Profits: {Gi_Date}  ({GreatestIncrease})")
print(f"Greatest Decrease in Profits: {Gd_Date} ({GreatestDecrease})")

#Saving to a txt file
text_file = open("PyBank_Results.txt", "w")
with open("PyBank_Results.txt", "w") as text_file:
    print("Financial Analysis" + '\n' +
    ("-"*25) + '\n' +
    (f"Total Months: {Months}") + '\n' +
    (f"Total: {Total_Funds}") + '\n' +
    (f"Average Change:  {Average}") + '\n' +
    (f"Greatest Increase in Profits: {Gi_Date}  ({GreatestIncrease})") + '\n' +
    (f"Greatest Decrease in Profits: {Gd_Date} ({GreatestDecrease})"), file=text_file)
text_file.close()