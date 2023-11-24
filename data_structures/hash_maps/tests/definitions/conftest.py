#------------------------------------------------------#
# Example: tests/definitions/conftest.py               #
#------------------------------------------------------#
#
# import pytest
# from definitions.samukasmk_example import ExampleA
#
#
# @pytest.fixture(scope='function')
# def example_a():
#     return ExampleA()


#------------------------------------------------------#
# Example: tests/definitions/test_samukasmk_example.py #
#------------------------------------------------------#
#
# from definitions.samukasmk_example import ExampleA
#
#
# def test_example_a():
#     example_a = ExampleA()
#     assert example_a.field_a == 'Example: 1'
#     assert example_a.field_b == 'Example: 2'
#     assert example_a.field_c == 'Example: 3'
# 
# 
# def test_example_a_local_conftest_(example_a):
#     assert example_a.field_a == 'Example: 1'
#     assert example_a.field_b == 'Example: 2'
#     assert example_a.field_c == 'Example: 3'
# 
# 
# def test_example_a_global_conftest(fourty_two):
#     assert fourty_two == 42
# 