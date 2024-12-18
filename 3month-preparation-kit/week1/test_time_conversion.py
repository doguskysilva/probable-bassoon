import pytest


def time_conversion(timestamp):
    hour = int(timestamp[0:2])
    isPM = timestamp[-2:] == "PM"
    newTime = timestamp[0:-2]

    if hour < 12 and isPM:
        newHour = hour + 12
        newTime = str(newHour) + newTime[2:]
    elif hour == 12 and isPM == False:
        newTime = "00" + newTime[2:]

    return newTime


def time_conversion_pythonic(timestamp):
    hour = int(timestamp[0:2])
    isPM = timestamp[-2:] == "PM"

    hours = hour % 12 + (12 if isPM else 0)

    return f"{hours:02d}{timestamp[2:-2]}"


@pytest.mark.parametrize(
    "test_input,test_expected",
    [
        ("07:05:45PM", "19:05:45"),
        ("12:01:00AM", "00:01:00"),
        ("12:01:00PM", "12:01:00"),
    ],
)
def test_time_conversion(test_input, test_expected):
    assert time_conversion(test_input) == test_expected
    assert time_conversion_pythonic(test_input) == test_expected
