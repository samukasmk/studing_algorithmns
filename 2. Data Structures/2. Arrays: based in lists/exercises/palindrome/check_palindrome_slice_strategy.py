# you can define helper methods if needed
def is_palindrome_slice_strategy(s):
    if s is None or len(s) == 0:
        return False

    return s == s[::-1]


class TestIStringIsPalindrome:

    def test_a_palindrome_string(self):
        assert is_palindrome_slice_strategy('madam') is True
        assert is_palindrome_slice_strategy('radar') is True

    def test_a_non_palindrome_string(self):
        assert is_palindrome_slice_strategy('non palindrome string') is False

    def test_a_null_value(self):
        assert is_palindrome_slice_strategy(None) is False

    def test_an_empty_string(self):
        assert is_palindrome_slice_strategy('') is False


if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])
