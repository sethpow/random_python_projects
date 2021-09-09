import pytest

def fizzBuzz(value):
    if is_multiple(value, 15):
        return 'FizzBuzz'
    if is_multiple(value, 3):
        return 'Fizz'
    if is_multiple(value, 5):
        return 'Buzz'
    
    return str(value)

def is_multiple(value, mod):
    return (value % mod) == 0

# def test_canCallFizzBuzz():
#     fizzBuzz(1)

def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal

def test_returns1With1PassedIn():
    # retVal = fizzBuzz(1)
    # assert retVal == '1'
    checkFizzBuzz(1, '1')

def test_returns2With2PassedIn():
    # retVal = fizzBuzz(1)
    # assert retVal == '1'
    checkFizzBuzz(2, '2')

def test_returnsFizzWith3PassedIn():
    # retVal = fizzBuzz(1)
    # assert retVal == '1'
    checkFizzBuzz(3, 'Fizz')

def test_returnsBuzzWith5PassedIn():
    # retVal = fizzBuzz(1)
    # assert retVal == '1'
    checkFizzBuzz(5, 'Buzz')

def test_returnsFizzBuzzWith15PassedIn():
    # retVal = fizzBuzz(1)
    # assert retVal == '1'
    checkFizzBuzz(15, 'FizzBuzz')