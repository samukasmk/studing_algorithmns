def reverse_int_by_string_positions(n):
    s = str(n)[::-1]
    return int(s)

class TestReverseIntegerByStringStrategy:

    def test_reverse_int_by_string_positions(self):
        assert reverse_int_by_string_positions(1234) == 4321
        assert reverse_int_by_string_positions(123) == 321
        assert reverse_int_by_string_positions(12) == 21
        assert reverse_int_by_string_positions(1) == 1


if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])