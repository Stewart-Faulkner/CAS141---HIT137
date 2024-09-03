from transformers import AutoTokenizer
from collections import Counter
import csv

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# File paths
input_file = r'K:\New folder\Assignment 2\output.txt'
output_csv_3_2 = r'K:\New folder\Assignment 2\top_30_tokens.csv'

def count_unique_tokens(file_path, chunk_size=1000000):
    token_counter = Counter()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            # Tokenize the chunk
            tokens = tokenizer.tokenize(chunk)
            
            # Update the counter
            token_counter.update(tokens)
            
            print(f"Processed {f.tell()} bytes")
    
    return token_counter

def main():
    print("Counting unique tokens...")
    token_counter = count_unique_tokens(input_file)
    
    # Get the top 30 tokens
    top_30_tokens = token_counter.most_common(30)
    
    # Write results to CSV file
    with open(output_csv_3_2, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Token', 'Count'])
        writer.writerows(top_30_tokens)
    
    print(f"Task 3.2: Top 30 most common tokens have been written to {output_csv_3_2}")
    
    # Print results
    print("\nTask 3.2: Top 30 most common tokens:")
    for token, count in top_30_tokens:
        print(f"{token}: {count}")

if __name__ == "__main__":
    main()
