# 
import os

import csv

csv_path = os.path.join('Resources', 'budget_data.csv')

# Open and read csv
with open(csv_path) as csv_file :
    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_reader)
   
# Assign variables  

    csv_list = list(csv_reader)
  
    profit_loss = []
    change = [] 
    months = []
    
# Calculate the total number of months  
# Calculate the total sum of Profit/Loss
    for row in csv_list:
        months.append(row[0])
        profit_loss.append(int(row[1]))
      
    total_months = len(months)
    total_sum = sum(profit_loss)
    
# Calculate the changes in Profit/Loss over the entire period
    for i in range(1, total_months):
        change = profit_loss[i] - profit_loss[i - 1]
        changes.append(change)

# Calculate the average change
    average_change = sum(changes) / len(changes)


# Find the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]

# Find the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

# Print the analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {num_rows}")
print(f"Total: $ {total_sum}")
print(f"Average Change: $ {average_change:.2f}")
print(f"Greatest Increase in Profits:{greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits:{greatest_decrease_date} (${greatest_decrease})")

# Export the results to a text file
output_file_path = "financial_analysis.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {num_rows}\n")
    
    output_file.write(f"Total: $ {total_sum}\n")
    
    output_file.write(f"Average Change: $ {average_change:.2f}\n")
    
    output_file.write(f"Greatest Increase in Profits:{greatest_increase_date} ${greatest_increase}\n")    
    output_file.write(f"Greatest Decrease in Profits:{greatest_decrease_date} ${greatest_decrease}\n")
    
print(f"\nAnalysis has been exported to {output_file_path}")

