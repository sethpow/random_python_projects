import pytest
from line_reader import readFromFile
from unittest.mock import MagicMock

# can call readFromFile
# readFromFile returns correct string
# readFromFile throws exception when file does not exist

# read and return first line from a file
# def test_canCallReadFromFile():
#     readFromFile('blah')


@pytest.fixture
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value = 'test line')
    mock_open = MagicMock(return_value = mock_file)
    monkeypatch.setattr('builtins.open', mock_open)
    return mock_open


# open file, read line, and return it
# dont want to open file in test
# instead, mock out the open fn and return a magicmock obj
# add readline attr to the mock (which is also a magicmock obj) that will return the test string
# then call the readFromFile fn
# when that call returns, validate that the open fn was called with correct params, and the expected test string was returned
def test_returnsCorrectString(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr('os.path.exists', mock_exists)

    result = readFromFile('blah')
    mock_open.assert_called_once_with('blah', 'r')
    assert result == 'test line'


def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr('os.path.exists', mock_exists)
    with pytest.raises(Exception):
        result = readFromFile('blah')