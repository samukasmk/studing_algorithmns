def reverse_string(s):
    s_chars = list(s)
    begin_index = 0
    end_index = len(s_chars) - 1
    while begin_index < end_index:
        s_chars[begin_index], s_chars[end_index] = s_chars[end_index], s_chars[begin_index]
        begin_index += 1
        end_index -= 1
    return ''.join(s_chars)


# you can define helper methods if needed
def is_palindrome_reverse_array(s):
    if s is None or len(s) == 0:
        return False
    return s == reverse_string(s)


class TestIStringIsPalindrome:

    def test_a_palindrome_string(self):
        assert is_palindrome_reverse_array('madam') is True
        assert is_palindrome_reverse_array('radar') is True

    def test_a_non_palindrome_string(self):
        assert is_palindrome_reverse_array('non palindrome string') is False

    def test_a_null_value(self):
        assert is_palindrome_reverse_array(None) is False

    def test_an_empty_string(self):
        assert is_palindrome_reverse_array('') is False


if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])
