import re
from collections import Counter
import csv
import multiprocessing as mp

# File paths
input_file = r'K:\New folder\Assignment 2\output.txt'
output_csv_3_1 = r'K:\New folder\Assignment 2\task_3.1.csv'

# Define some common non-noun words and numerals to exclude
common_non_nouns = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 
                        'from', 'up', 'about', 'than', 'then', 'that', 'which', 'his', 'her', 'he', 'she', 'it', 
                        'they', 'we', 'you', 'who', 'whom', 'whose', 'where', 'when', 'why', 'how', 'all', 'any',
                        'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only',
                        'own', 'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'should', 'there', 'here', 'now'])

number_words = set(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
                    'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million', 'billion',
                    'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'last', 'tenth'])

# Meaningless words to remove
unwanted_words = set(['inr', 'wbc', 'pt', 'neg', 'po', 'sig', 'ct', 'dr', 'refills', 'disp', 'fax', 'md', 'hct'])

def is_potential_noun(word):
    lower_word = word.lower()
    return (word[0].isupper() or word.isupper()) and word.isalpha() and len(word) > 1 and \
           lower_word not in common_non_nouns and lower_word not in number_words and not lower_word.isdigit()

def process_chunk(chunk):
    # Use regular expressions to split words, keeping capitalized or fully uppercase words
    words = re.findall(r'\b[A-Z][a-z]+\b|\b[A-Z]+\b', chunk)
    return Counter(word.lower() for word in words if is_potential_noun(word))

def count_nouns_parallel(file_path, chunk_size=1000000):  # Approximately 1MB chunks
    noun_counter = Counter()
    
    def read_in_chunks(file_object, chunk_size):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

    with open(file_path, 'r', encoding='utf-8') as f:
        with mp.Pool() as pool:
            for counter in pool.imap_unordered(process_chunk, read_in_chunks(f, chunk_size)):
                noun_counter.update(counter)
                print(f"Processed a chunk. Total processed potential nouns: {sum(noun_counter.values())}")

    return noun_counter

def main():
    print("Counting potential nouns (excluding numerals)...")
    noun_counter = count_nouns_parallel(input_file)
    
    # Get the top 30 most common potential nouns
    top_30_nouns = noun_counter.most_common(30)
    
    # Filter out meaningless words
    filtered_nouns = [(noun, count) for noun, count in top_30_nouns if noun not in unwanted_words]
    
    # Write results to a CSV file
    with open(output_csv_3_1, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['noun', 'count'])
        writer.writerows(filtered_nouns)
    
    print(f"Task 3.1: Top 30 most common potential nouns have been written to {output_csv_3_1}")
    
    # Print results
    print("\nTask 3.1: Top 30 most common potential nouns:")
    for noun, count in filtered_nouns:
        print(f"{noun}: {count}")

if __name__ == "__main__":
    main()
