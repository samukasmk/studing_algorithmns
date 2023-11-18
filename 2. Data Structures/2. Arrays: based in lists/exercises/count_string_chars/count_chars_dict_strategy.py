def count_characters(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

string = "Hello, World!"
result = count_characters(string)
assert result == {'l': 3, 'o': 2, 'H': 1, 'e': 1, ',': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}
print(result)
