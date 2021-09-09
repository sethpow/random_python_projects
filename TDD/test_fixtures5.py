import pytest

@pytest.fixture(params=[1, 2, 3])
def setup(request):
    retVal = request.param
    print(f'\nSetup:  retVal: {retVal}')
    return retVal


def test1(setup):
    print(f'\nTest1 setup: {setup}')
    assert True