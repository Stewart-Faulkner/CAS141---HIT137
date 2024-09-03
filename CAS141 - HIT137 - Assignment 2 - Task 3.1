import spacy
from collections import Counter
import csv

# Load the English model
nlp = spacy.load("en_core_web_sm")

# File paths
input_file = r'K:\New folder\Assignment 2\output.txt'
output_csv_3_1 = r'K:\New folder\Assignment 2\top_30_nouns.csv'

# Initialize a Counter for noun frequency
noun_counter = Counter()

# Set chunk size for processing large files
chunk_size = 100000  # Reduced chunk size to accommodate spaCy processing

def extract_nouns(doc):
    """
    Extract nouns from the given spaCy document.
    Ignore stop words, digits, and single-character words.
    Return lemmatized forms of the nouns.
    """
    return [token.lemma_ for token in doc if token.pos_ == "NOUN" 
            and not token.is_stop and not token.is_digit and len(token) > 1]

# Process the input file in chunks
with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read(chunk_size)
    while text:
        # Process the chunk with spaCy
        doc = nlp(text)
        # Extract nouns and update the counter
        nouns = extract_nouns(doc)
        noun_counter.update(nouns)
        # Print progress
        print(f"Processed {f.tell()} bytes")
        # Read the next chunk
        text = f.read(chunk_size)

# Get the top 30 most common nouns
top_30_nouns = noun_counter.most_common(30)

# Write results to CSV file
with open(output_csv_3_1, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Noun', 'Count'])
    writer.writerows(top_30_nouns)

print(f"Task 3.1: Top 30 most common nouns have been written to {output_csv_3_1}")

# Print results
print("\nTask 3.1: Top 30 most common nouns:")
for noun, count in top_30_nouns:
    print(f"{noun}: {count}")
