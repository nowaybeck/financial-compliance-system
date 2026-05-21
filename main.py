from src.data_loader import load_data
from src.feature_engineering import extract_features

import random

# Load dataset
texts, labels = load_data()

print("Total samples:", len(texts))

# Print 5 random samples
for i in random.sample(range(len(texts)), 5):

    text = texts[i]

    # Generate features from text
    features = extract_features(text)

    print("\nTEXT:", text)

    print("FEATURES:", features)

    print("LABEL:", labels[i])

    print("-" * 60)