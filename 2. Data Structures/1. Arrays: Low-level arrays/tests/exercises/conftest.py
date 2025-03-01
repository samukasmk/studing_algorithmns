import pytest
from exercises.some_exercises import ExerciseA


@pytest.fixture(scope='function')
def exercise_a():
    return ExerciseA()
