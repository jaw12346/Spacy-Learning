import spacy

nlp = spacy.blank("en")  # Creates a blank English model

print('Part 1\n-----------------------------')

doc = nlp("Hello, world! This is my first text with Spacy.")

print(doc.text)  # Output: Hello, world! This is my first text with Spacy.
first_token = doc[0]
print(first_token, first_token.text)  # Output: Hello Hello

slice = doc[2:5]  # Slice of the doc
print(slice.text)  # Output: world! This

# ------------------------------
print('\n\nPart 2\n-----------------------------')

doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are. Twenty years ago, the world had 1.9 billion people..."
)
# Iterate over the tokens in the doc
for token in doc:
    if token.like_num:  # Check if the token resembles a number
        next_token = doc[token.i + 1]
        if next_token.text == "%":  # Check if the next token's text is % --> Is a percentage
            print("Percentage found:", token.text)
        else:
            print("Number found:", token.text)
    # Detects: 1990, 60, 4, twenty, 1.9, billion

