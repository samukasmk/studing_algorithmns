from exercises.some_exercises import ExerciseA


def test_exercise_a():
    exercise_a = ExerciseA()
    assert exercise_a.field_a == 'Exercise: A'
    assert exercise_a.field_b == 'Exercise: B'
    assert exercise_a.field_c == 'Exercise: C'


def test_local_conftest(exercise_a):
    assert exercise_a.field_a == 'Exercise: A'
    assert exercise_a.field_b == 'Exercise: B'
    assert exercise_a.field_c == 'Exercise: C'


def test_global_conftest(fourty_two):
    assert fourty_two == 42
