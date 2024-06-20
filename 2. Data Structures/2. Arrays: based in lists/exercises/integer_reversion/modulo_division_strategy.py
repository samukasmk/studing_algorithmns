def integer_reverse_by_modulo_division(n):
    reversed = 0
    remainder = 0
    while n > 0:
        remainder = n % 10
        reversed = reversed * 10 + remainder
        n = n // 10
    return reversed


class TestReverseIntegerByModuloDivisionStrategy:

    def test_reverse_int_by_string_positions(self):
        assert integer_reverse_by_modulo_division(1234) == 4321
        assert integer_reverse_by_modulo_division(123) == 321
        assert integer_reverse_by_modulo_division(12) == 21
        assert integer_reverse_by_modulo_division(1) == 1
