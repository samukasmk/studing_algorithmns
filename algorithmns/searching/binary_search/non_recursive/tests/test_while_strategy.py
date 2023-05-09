import pytest
from random import randint
from ..while_strategy import binary_search


@pytest.mark.timeout(1)
@pytest.mark.parametrize("existing_element", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
def test_binary_search_slice_unique_short_list_existing_element(unique_short_list, existing_element):
    """ Search EXISTING elements in unique short list """
    search_result = binary_search(unique_short_list, existing_element)
    assert search_result is True


@pytest.mark.timeout(1)
@pytest.mark.parametrize("non_existing_element", [-5, -4, -3, -2, -1, 0, 13, 14, 15, 16, 17, 18])
def test_binary_search_slice_unique_short_list_non_existing_element(unique_short_list, non_existing_element):
    """ Search NON existing elements in short list """
    search_result = binary_search(unique_short_list, non_existing_element)
    assert search_result is False


@pytest.mark.timeout(1)
@pytest.mark.parametrize("existing_element", [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_binary_search_slice_repeated_short_list_existing_element(repeated_short_list, existing_element):
    """ Search EXISTING elements in repeated short list """
    search_result = binary_search(repeated_short_list, existing_element)
    assert search_result is True


@pytest.mark.timeout(1)
@pytest.mark.parametrize("non_existing_element", [-5, -4, -3, -2, -1, 0, 13, 14, 15, 16, 17, 18])
def test_binary_search_slice_repeated_short_list_non_existing_element(repeated_short_list, non_existing_element):
    """ Search NON existing elements in repeated short list """
    search_result = binary_search(repeated_short_list, non_existing_element)
    assert search_result is False


@pytest.mark.timeout(60)
def test_binary_search_slice_billionaire_list_non_existing_element(billionaire_list):
    """ Search EXISTING elements in huge list of billion elements """
    for existing_element in [billionaire_list[randint(0, 999999)] for i in range(101)]:
        search_result = binary_search(billionaire_list, existing_element)
        assert search_result is True


@pytest.mark.timeout(60)
def test_binary_search_slice_billionaire_list_non_existing_negative_element(billionaire_list):
    """ Search NON existing elements in repeated short list """
    for non_existing_element in [randint(-99999, 0) for i in range(51)]:
        assert non_existing_element not in billionaire_list

        search_result = binary_search(billionaire_list, non_existing_element)
        assert search_result is False


@pytest.mark.timeout(60)
def test_binary_search_slice_billionaire_list_non_existing_positive_element(billionaire_list):
    """ Search NON existing elements in repeated short list """
    for non_existing_element in [randint(999999, 9999999) for i in range(51)]:
        assert non_existing_element not in billionaire_list

        search_result = binary_search(billionaire_list, non_existing_element)
        assert search_result is False
