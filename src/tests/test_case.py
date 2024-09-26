import pytest

@pytest.mark.slow
def test_slow_operation():
    pass


def test_addition():
    print('testing...')
    assert 1 + 1 == 2


def test_subtraction():
    assert 5 - 3 == 2
