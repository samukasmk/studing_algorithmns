"""
    your algorithm goes here
    return True if str1 and str2 are anagrams, otherwise return False
"""


def array_map_chars_count(s):
    chars_map = [0] * 256
    for c in s:
        ordinal_index = ord(c)
        chars_map[ordinal_index] += 1
    return chars_map


def is_anagram(str1, str2):
    return array_map_chars_count(str1) == array_map_chars_count(str2)


class TestAnagramArrayOrd():
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

