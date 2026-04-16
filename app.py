from textblob import TextBlob

def analyze(text):
    if not isinstance(text, str):
        return "Error: not a string"

    if text.strip() == "":
        return "Error: empty input"

    polarity = TextBlob(text).sentiment.polarity
    if polarity >= 0.1:
        sentiment = "Positive"
    elif polarity <= -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 3)
    }

test_sentences = [
    "I love this!",
    "This is amazing",
    "Great job",
    "Very happy with it",

    "I hate this",
    "This is terrible",
    "Worst experience ever",
    "I am disappointed",

    "The meeting is at 3 PM",
    "I went to school",
    "It is a book",
    "Weather is normal today",
]

print("\n=== SENTIMENT RESULTS ===\n")

for t in test_sentences:
    print(t, "->", analyze(t))