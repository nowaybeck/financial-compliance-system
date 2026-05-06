from src.data_loader import load_data
import random

texts, labels = load_data()

print("Total samples:", len(texts))

# Print 5 random samples
for i in random.sample(range(len(texts)), 5):
    print("\nTEXT:", texts[i])
    print("LABEL:", labels[i])