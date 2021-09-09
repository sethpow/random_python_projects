from pytest import raises


# want to verify that a function throws an exception under certain conditions
# pytest provides this verification using the "with" keyword
# if the specified exception is not raised in the code block specified after the "raises"line, then the test fails

def raises_value_exception():
    # pass
    raise ValueError

def test_exception():
    with raises(ValueError):
        raises_value_exception()