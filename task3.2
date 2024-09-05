from transformers import AutoTokenizer
from collections import Counter
import csv
import concurrent.futures
import multiprocessing
import re

# Updated file paths
input_file = r'C:\Users\elegy\Assignment 2\output.txt'
output_csv_3_2 = r'C:\Users\elegy\Assignment 2\task_3.2_optimized.csv'

# Load AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# A refined stopwords list, combining user-defined and common meaningless content
stopwords = set([
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
    'of', 'with', 'by', 'from', 'up', 'about', 'than', 'then', 'that', 
    'which', 'his', 'her', 'he', 'she', 'it', 'they', 'we', 'you', 'who', 
    'whom', 'whose', 'where', 'when', 'why', 'how', 'all', 'any', 'both', 
    'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 
    'not', 'only', 'own', 'same', 'so', 'too', 'very', 'can', 'will', 
    'just', 'should', 'there', 'here', 'now', 'is', 'as', 'was', 'were', 
    'has', 'have', 'are', 'be', 'this', 'that', 'these', 'those', 'am', 'i', 'it\'s', 
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'mg', 'po', 'si', 'pt', 'ne', 'mc', 'ct', 'di', 'hc',
    'had', 'per', 'your',
    'first', 'last', 'daily', 'normal', 'right', 'left',
    'day', 'date',
    'st', 'pl', 'ex', 'un', 'cr', 'ed', 'dr', 'ao',
    'times', 'hours', 'time',
    'well'
])

# Meaningless symbols and single letters
symbols = set(['*', '.', '-', ':', ',', '[', ']', '(', ')', '/', '##s', '##g', '##', '\'', '"', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

def process_chunk(chunk):
    # Use AutoTokenizer for tokenization
    tokens = tokenizer.tokenize(chunk)
    
    # Filter out stopwords and symbols
    nouns = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stopwords and token not in symbols]
    
    if not nouns:
        print("Warning: No valid tokens found in this chunk!")
    
    return Counter(nouns)

def read_in_dynamic_chunks(file_object, chunk_size=1000000):
    chunk = ""
    for line in file_object:
        if len(chunk) + len(line) > chunk_size:
            yield chunk
            chunk = line
        else:
            chunk += line
    if chunk:
        yield chunk

def count_nouns_parallel(file_path, chunk_size=1000000):  # Dynamic chunking, with a maximum chunk size
    noun_counter = Counter()

    num_workers = multiprocessing.cpu_count()  # Use the number of CPU cores
    with open(file_path, 'r', encoding='utf-8') as f:
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:  # Use a thread pool
            futures = [executor.submit(process_chunk, chunk) for chunk in read_in_dynamic_chunks(f, chunk_size)]
            for future in concurrent.futures.as_completed(futures):
                noun_counter.update(future.result())

    return noun_counter

def main():
    print("Extracting tokens and counting using AutoTokenizer...")
    noun_counter = count_nouns_parallel(input_file, chunk_size=1000000)  # Maximum chunk size is 1,000,000 characters
    
    # Get the top 30 most common words
    top_30_nouns = noun_counter.most_common(30)
    
    if not top_30_nouns:
        print("Warning: No valid tokens found in the entire file!")

    # Write the results to a CSV file
    with open(output_csv_3_2, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['token', 'count'])
        writer.writerows(top_30_nouns)
    
    print(f"Task 3.2: The top 30 most common words have been written to {output_csv_3_2}")
    
    # Print the results
    print("\nTask 3.2: The top 30 most common words:")
    for token, count in top_30_nouns:
        print(f"{token}: {count}")

if __name__ == "__main__":
    main()
