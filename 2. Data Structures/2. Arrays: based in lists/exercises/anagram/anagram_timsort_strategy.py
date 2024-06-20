"""
Runtime complexity: O(nlog)
Space complexity: O(n)
"""


def is_anagram(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


class TestAnagramSorted():
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
