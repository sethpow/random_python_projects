import pytest

def test_intassert():
    assert 1 == 1

def test_strassert():
    assert '1' == '1'

def test_floatassert():
    assert 1.0 == 1.0

def test_approxfloatassert():
    assert 0.1 + 0.2 == pytest.approx(0.3)

def test_arrayassert():
    assert [1, 2, 3] == [1, 2, 3]

def test_dictassert():
    assert {'name': 'seth'} == {'name': 'seth'}