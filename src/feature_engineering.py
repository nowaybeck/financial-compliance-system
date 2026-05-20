#re - Python’s Regular Expression module
import re
RISK_KEYWORDS = [
    "loss",
    "decline",
    "penalty",
    "lawsuit",
    "risk",
    "regulation",
    "non-compliance",
    "fine",
    "debt",
    "failure"
]

POSITIVE_KEYWORDS = [
    "growth",
    "profit",
    "gain",
    "improvement",
    "success"
]

def count_keywords(text,keywords):
    count = 0

    for word in keywords:
        if word in text:
            count+=1
    return count 

def count_numbers(text):
    numbers = re.findall(r"\d+",text) #\d+ -> '2024' 
    #what 'r' does is it tells the python interpreter to treat it as a raw string and pass it to the regex engine as it is.
    return len(numbers)

def count_negations(text):
    negations = ["not", "no", "never", "none"]
    count = 0

    for word in negations:
        if word in text:
            count+=1
    return count

def extract_features(text):
    text = text.lower()

    # Feature 1 → sentence length ex- len("hello") = 5
    sentence_length = len(text) 

    # Feature 2 → risky words count
    risk_word_count = count_keywords(text, RISK_KEYWORDS)

    # Feature 3 → positive words count
    positive_word_count = count_keywords(text, POSITIVE_KEYWORDS)

    # Feature 4 → number count
    number_count = count_numbers(text)

    # Feature 5 → negation count
    negation_count = count_negations(text)

    features = [sentence_length,
                risk_word_count,
                positive_word_count,
                number_count,
                negation_count]
    return features