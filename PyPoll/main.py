import csv
import os
from collections import Counter


# Function to read data from a CSV file
def read_data(file_path):
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip the header
        data = list(csvreader)  # Read the rest of the data
    return data


# Function to calculate the total number of votes
def calculate_total_votes(data):
    return len(data)


# Function to calculate the number of votes each candidate received
def calculate_votes(data):
    votes = [row[2] for row in data]  # Extract the candidate names (votes)
    vote_count = Counter(votes)  # Count the votes for each candidate
    return vote_count


# Function to print the election results and write them to a text file
def print_and_write_results(total_votes, vote_count):
    # Prepare the results string
    results = ("Election Results\n"
               "-------------------------\n"
               f"Total Votes: {total_votes}\n"
               "-------------------------\n")

    for candidate, votes in vote_count.items():
        percentage = (votes / total_votes) * 100  # Calculate the vote percentage for each candidate
        results += f"{candidate}: {percentage:.3f}% ({votes})\n"  # Add the candidate's results to the results string

    results += "-------------------------\n"

    winner = max(vote_count, key=vote_count.get)  # Determine the winner
    results += f"Winner: {winner}\n"  # Add the winner to the results string

    results += "-------------------------\n"

    print(results)  # Print the results

    # Check if 'analysis' directory exists, if not create it
    if not os.path.exists('analysis'):
        os.makedirs('analysis')

    # Write the results to a text file
    with open('analysis/results.txt', 'w') as file:
        file.write(results)


# Main function to run the election analysis
def main():
    data = read_data('Resources/election_data.csv')  # Read data

    total_votes = calculate_total_votes(data)  # Calculate total votes

    vote_count = calculate_votes(data)  # Calculate vote count

    print_and_write_results(total_votes, vote_count)  # Print and write results


# Call the main function
if __name__ == "__main__":
    main()
