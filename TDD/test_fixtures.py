import pytest


# applies to all tests (see test3)
@pytest.fixture(autouse=True)
def setup():
    print('\nSetup')


def test1(setup):
    print('Executing test1')
    assert True


@pytest.mark.usefixtures('setup')
def test2():
    print('Executing test2')
    assert True


def test3():
    print('Executing test3')
    assert True