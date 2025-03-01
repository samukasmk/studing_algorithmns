from collections import Counter

def count_characters(string):
    char_counts = Counter(string)
    return char_counts

string = "Hello, World!"
result = count_characters(string)
assert result == Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ',': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1})
print(result)
