# add dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the data file.
with open(file_to_load) as election_data:

     # To do: perform analysis.
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    #for row in file_reader:
       # print(row)


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")

# Write down the names of all the candidates.

# Add a vote count for each candidate.

# Get the total votes for each candidate.

# Get the total votes cast for the election.
