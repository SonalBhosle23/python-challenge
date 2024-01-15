#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 
import os

import csv

csv_path = os.path.join('Resources', 'election_data.csv')


# In[12]:


# Open and read csv
with open(csv_path) as csv_file :
    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_reader)
    #print(csv_header)

# Assign variables  

    csv_list = list(csv_reader)
  
    ballot_id = []
    county = [] 
    candidate_counts = {}
    max_percentage_candidate = None
    max_percentage = 0
    
# Calculate the total number of votes cast
    for row in csv_list:
        ballot_id.append(row[0])
        candidate_name = (row[2])
        if candidate_name in candidate_counts:
            candidate_counts[candidate_name] += 1
        else:
            candidate_counts[candidate_name] = 1
    total_votes = len(ballot_id)
    unique_candidates_count = len(candidate)

    
# Print Election result analysis
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
#print('Candidate Counts:')
for candidate, count in candidate_counts.items():
    #print(f'{candidate}: {count} votes')
    percentage = (count / total_votes) * 100
    print(f'{candidate}: {percentage:.3f}% ({count}) ')
    if percentage > max_percentage:
            max_percentage = percentage
            max_percentage_candidate = candidate

print("-----------------------------")
print(f"Winner: {max_percentage_candidate}")

# Export the results to a text file
output_file_path = "Election Results.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("------------------\n")

    output_file.write(f"{candidate}: {percentage:.3f}% ({count})\n")
    output_file.write("------------------\n")
    output_file.write(f"Winner: {max_percentage_candidate}\n")
    
print(f"\nAnalysis has been exported to {output_file_path}")


# In[ ]:




