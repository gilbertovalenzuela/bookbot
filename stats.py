def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_occurrences(text):
    lower_text = text.lower()
    occurrences = {}

    for letter in lower_text:
        if letter in occurrences:
            occurrences[letter] += 1
        else:
            occurrences[letter] = 1
    return occurrences

def get_sorted_occurrences(text):
    occurrences = get_num_occurrences(text)
    sorted_occurrences = []

    for letter in occurrences:
        sorted_occurrences.append({"char": letter, "num": occurrences[letter]})

    sorted_occurrences.sort(reverse=True, key=lambda x: x["num"])
    return sorted_occurrences