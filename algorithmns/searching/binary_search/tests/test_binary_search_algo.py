import pytest

@pytest.mark.parametrize("sample_test_parameter", [1, 2, 3, 4])
def test_pytest_structure(sample_fixture, sample_test_parameter):
    assert sample_fixture == 42
    assert 1 <= sample_test_parameter <= 4