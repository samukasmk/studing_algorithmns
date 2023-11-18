import pytest
from examples.some_examples import ExampleA


@pytest.fixture(scope='function')
def example_a():
    return ExampleA()
