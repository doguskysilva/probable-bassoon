import pytest


def template(var):
    return None


def template_pythonic(var):
    return None


@pytest.mark.parametrize(
    "test_input,test_expected",
    [
        (None, None),
    ],
)
def test_template(test_input, test_expected):
    assert template(test_input) == test_expected
    assert template_pythonic(test_input) == test_expected
