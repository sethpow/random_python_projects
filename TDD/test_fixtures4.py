import pytest

@pytest.fixture(scope='session', autouse=True)
def setup_session():
    print('\nSetup session')


@pytest.fixture(scope='module', autouse=True)
def setup_module():
    print('\nSetup module')


@pytest.fixture(scope='class', autouse=True)
def setup_class():
    print('\nSetup class')


@pytest.fixture(scope='function', autouse=True)
def setup_function():
    print('\nSetup function')


class Test_Class:
    def test_it(self):
        print('Test_it')
        assert True

    def test_it2(self):
        print('Test_it2')
        assert True