import os
import csv

budget_data = os.path.join("budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_months +=1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    for row in csvreader:
            dates.append(row[0])

            change = int(row[1])-value
            profits.append(change)
            value = int(row[1])

            total_months +=1

            