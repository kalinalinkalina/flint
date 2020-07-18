import os
import sys
import csv
from datetime import date, datetime, timedelta

input_path = "data/flint_noNAs_noExpectedLead.csv"
output_path = "data/flint_months_noNAs_noExpectedLead.csv"

start_date = date(1998, 12, 30)

with open(input_path, newline='\n') as in_file, open(output_path, 'w', newline='\n') as out_file:
    reader = csv.reader(in_file, delimiter=',')
    writer = csv.writer(out_file, delimiter=',')
    for row in reader:
        day = row[3]
        if "Time" not in day:
            delta = timedelta(days=int(day))
            current_date = start_date + delta
            months_since_start = (current_date.year - start_date.year) * 12 + current_date.month - start_date.month
            print(months_since_start)
            
            row[3] = months_since_start
            writer.writerow(row)
            