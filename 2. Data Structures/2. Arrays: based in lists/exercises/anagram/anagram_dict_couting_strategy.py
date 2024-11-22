def build_char_frequency(s):
    s = s.replace(" ", "").lower()
    char_frequency = {}
    for char in s:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    return char_frequency

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    return build_char_frequency(str1) == build_char_frequency(str2)

class TestAnagramDict():
    def test_is_anagram_true(self):
        assert is_anagram('eat', 'tea') is True
        assert is_anagram('listen', 'silent') is True
    def test_is_not_an_anagram(self):
        assert is_anagram('anagram', 'non anagram') is False


if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])
