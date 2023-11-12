import csv
import os


# Function to read data from a CSV file
def read_data(file_path):
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip the header
        data = list(csvreader)  # Read the rest of the data
    return data


# Function to calculate the total number of months
def calculate_total_months(data):
    return len(data)


# Function to calculate the net total amount of "Profit/Losses"
def calculate_net_total(data):
    return sum(int(row[1]) for row in data)


# Function to calculate the changes in "Profit/Losses" over the entire period
def calculate_changes(data):
    prev_net = int(data[0][1])
    changes = []
    for row in data[1:]:
        net_change = int(row[1]) - prev_net  # Calculate change from previous month
        prev_net = int(row[1])  # Update previous month's net
        changes.append(net_change)
    return changes


# Function to calculate the greatest increase in profits (date and amount) over the entire period
def calculate_greatest_increase(data, changes):
    max_change = max(changes)
    date = data[changes.index(max_change) + 1][0]  # Get date of greatest increase
    return date, max_change


# Function to calculate the greatest decrease in losses (date and amount) over the entire period
def calculate_greatest_decrease(data, changes):
    min_change = min(changes)
    date = data[changes.index(min_change) + 1][0]  # Get date of greatest decrease
    return date, min_change


# Function to print the analysis results and write them to a text file
def print_and_write_results(total_months, net_total, average_change, greatest_increase, greatest_decrease):
    # Prepare the results string
    results = ("Financial Analysis\n"
               "----------------------------\n"
               f"Total Months: {total_months}\n"
               f"Total: ${net_total}\n"
               f"Average Change: ${average_change:.2f}\n"
               f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
               f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

    print(results)  # Print the results

    # Check if 'analysis' directory exists, if not create it
    if not os.path.exists('analysis'):
        os.makedirs('analysis')

    # Write the results to a text file
    with open('analysis/results.txt', 'w') as file:
        file.write(results)


# Main function to run the financial analysis
def main():
    data = read_data('Resources/budget_data.csv')  # Read data

    total_months = calculate_total_months(data)  # Calculate total months

    net_total = calculate_net_total(data)  # Calculate net total

    changes = calculate_changes(data)  # Calculate changes

    average_change = sum(changes) / len(changes)  # Calculate average change

    greatest_increase = calculate_greatest_increase(data, changes)  # Calculate greatest increase

    greatest_decrease = calculate_greatest_decrease(data, changes)  # Calculate greatest decrease

    print_and_write_results(total_months, net_total, average_change, greatest_increase,
                            greatest_decrease)  # Print and write results


# Call the main function
if __name__ == "__main__":
    main()
