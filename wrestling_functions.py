import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = os.path.join("..", "Resource", "WWE-Data-2016.csv")
# Define the function and have it accept the 'wrestlerData' as its sole parameter
def print_percentages(wrestler_data):
# Find the total number of matches wrestled
    total_matches = int(wrestler_data[1]) + int(wrestler_data[2]) + int(wrestler_data[3]) 
# Find the percentage of matches won
    percent_won = str((int(wrestler_data[1]) / total_matches) * 100)
# Find the percentage of matches lost
    percent_lost = str((int(wrestler_data[2]) / total_matches) * 100).format(":.00%")
# Find the percentage of matches drawn
    percent_draws = str((int(wrestler_data[3]) / total_matches) * 100)
# Print out the wrestler's name and their percentage stats
    name = wrestler_data[0]
    print(f"Wresler {name} \nwon {percent_won.} \nlost {percent_lost} \ndrew {percent_draws}")
    if float(percent_lost)>50.00:
        print(f"{name} is a Jobber")
    else:
        print(f"{name} is a Superstar")

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
