import pytest
from definitions.samukasmk_example import ExampleA


@pytest.fixture(scope='function')
def example_a():
    return ExampleA()
