# Task 1: Extract the ‘text’ in all the CSV files and store them into a single ‘.txt file’.

import os
import pandas as pd

# Specify the folder path containing CSV files
folder_path = r'K:\New folder\Assignment 2'
output_file = r'K:\New folder\Assignment 2\output.txt'

# Initialize an empty list to store all extracted texts
all_texts = []

# Iterate through all files in the specified folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):  # Only process CSV files
        file_path = os.path.join(folder_path, filename)
        
        # Read CSV file, try different encodings
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding='ISO-8859-1')
        
        print(f"Processing file: {filename}")
        print(df.head())  # Print first few rows to check format
        
        # Check for 'TEXT' or 'Text' column (case-insensitive)
        text_column = next((col for col in df.columns if col.lower() == 'text'), None)
        
        if text_column:
            texts = df[text_column].tolist()  # Convert column to list
            all_texts.extend(texts)  # Add texts from this file to the list
        else:
            print(f"'TEXT' column not found in file {filename}")

# Combine all texts into a single string, separated by newlines
combined_text = '\n'.join(str(text) for text in all_texts if pd.notna(text))

# Write the combined text to a .txt file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(combined_text)

print(f"Text from all CSV files has been written to {output_file}")
print(f"Total characters written: {len(combined_text)}")
