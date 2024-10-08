import spacy
import scispacy
from transformers import AutoTokenizer, AutoModel

# Load SpaCy models
print("Loading en_core_sci_sm model...")
nlp_sm = spacy.load("en_core_sci_sm")
print("en_core_sci_sm model loaded successfully!")

print("Loading en_ner_bc5cdr_md model...")
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")
print("en_ner_bc5cdr_md model loaded successfully!")

# Load BioBERT model
print("Loading BioBERT model...")
tokenizer = AutoTokenizer.from_pretrained("monologg/biobert_v1.1_pubmed")
model = AutoModel.from_pretrained("monologg/biobert_v1.1_pubmed")
print("BioBERT model loaded successfully!")

print("All libraries and models have been successfully loaded! Task 2 completed!")

# Simple test
test_text = "The patient was diagnosed with type 2 diabetes and prescribed metformin."

doc = nlp_sm(test_text)
print("\nEntity recognition results using en_core_sci_sm model:")
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")

doc = nlp_bc5cdr(test_text)
print("\nEntity recognition results using en_ner_bc5cdr_md model:")
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")

print("\nBioBERT tokenization example:")
tokens = tokenizer.tokenize(test_text)
print(tokens[:10])  # Print the first 10 tokens
