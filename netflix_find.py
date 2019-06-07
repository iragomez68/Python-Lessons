# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resource', 'netflix_ratings.csv')

video = input("What show or movie are you looking for? ")
# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module
with open(csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    found_video = False
    # Read each row of data after the header
    for row in csvreader:
        if row[0] == video:
            found_video = True
            print(f"{row[0]} is rated {row[1]} with a rating of {row[5]}")
            break

if found_video == False:
    print("Sorry video not found")
