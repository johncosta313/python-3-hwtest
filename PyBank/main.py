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

    