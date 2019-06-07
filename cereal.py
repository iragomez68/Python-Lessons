import os
import csv

csvpathInput = os.path.join("..", "Resource", "cereal.csv")

with open(csvpathInput,'r',encoding="utf8",newline="") as csvfileInput:
    csvreader = csv.reader(csvfileInput,delimiter=",")
    csv_header = next(csvreader, None)
    print(f"Header {csv_header}")
    for row in csvreader:
        fiberGrams = float(row[7])

        if fiberGrams >= 5.00:
            print(row)