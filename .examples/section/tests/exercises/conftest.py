import pytest
from exercises.samukasmk_exercise import ExerciseA


@pytest.fixture(scope='function')
def exercise_a():
    return ExerciseA()
