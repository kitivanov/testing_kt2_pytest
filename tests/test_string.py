import pytest

from src.main import string_length

@pytest.mark.parametrize("test_input,expected", [
    ("", 0),
    ("hello", 5),
    ("line1\nline2", 11),
    ("     ", 5),
])
def test_string_length(test_input, expected):
    assert string_length(test_input) == expected
