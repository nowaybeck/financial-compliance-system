from datasets import load_dataset

def load_data():
    dataset = load_dataset("financial_phrasebank", "sentences_allagree")
    data = dataset["train"]
    
    texts = data["sentence"]
    labels = data["label"]
    
    # Convert labels
    labels = [1 if l == 0 else 0 for l in labels]
    
    return texts, labels