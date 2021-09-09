import pytest

# production code
def str_len(the_str):
    return len(the_str)


# unit test
def test_string_length():
    test_str = '1'                      # setup
    result = str_len(test_str)          # action
    assert result == 1                  # assert