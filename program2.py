def analyze_paragraph(text):
    # Step 1: Convert text to lowercase
    text = text.lower()

    # Step 2: Remove punctuation by replacing symbols with spaces
    punctuation = ".,!?;:-_\"'"
    for symbol in punctuation:
        text = text.replace(symbol, " ")

    # Step 3: Split paragraph into a list of words
    words = text.split()

    # Step 4: Count frequency of each word using a basic dictionary
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] = freq_dict[word] + 1
        else:
            freq_dict[word] = 1

    # Step 5: Find the most frequent word
    most_frequent_word = ""
    max_count = 0

    for word in freq_dict:
        if freq_dict[word] > max_count:
            max_count = freq_dict[word]
            most_frequent_word = word

    # Step 6: Find the longest word repeated more than once (count > 1)
    longest_repeated_word = ""
    max_length = 0

    for word in freq_dict:
        if freq_dict[word] > 1:  # Appears more than once
            if len(word) > max_length:
                max_length = len(word)
                longest_repeated_word = word
            elif len(word) == max_length and word < longest_repeated_word:
                # Tie-breaker: choose alphabetically smaller word
                longest_repeated_word = word

    return most_frequent_word, max_count, longest_repeated_word



input_text = "The cat sat. The CAT ran! The dog barked, but the cat slept."
top_word, count, longest_word = analyze_paragraph(input_text)

print("Most frequent word:", f"'{top_word}' ({count} times)")
print("Longest repeated word:", f"'{longest_word}'.")
