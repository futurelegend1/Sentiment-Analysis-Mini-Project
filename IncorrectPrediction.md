##Case 1: "Weather is normal today"
Prediction: Positive(0.15)
Analysis:
This sentence is actually nautral in meaning, but the word "normal" slightly increased the polarity. TextBlob is dictionary based, so it can misinterpret the neutral statements as a positive sentiment.

##Case 2: "I went to school"
Prediction: Positive / Neutral
Analysis:
This sentence doesn't contain any emotional words, and some words
can slightly lean to a positive sentiment.