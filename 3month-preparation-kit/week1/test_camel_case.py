import pytest


def split_words(operable: str) -> str:
    output = ""

    for char in operable:
        if char.isalpha():
            if output != "" and char.isupper():
                output += " "

            output += char.lower()

    return output


def combine_words(operable: str, symbol: str) -> str:
    words = operable.title().split(" ")

    if symbol != "C":
        words[0] = words[0].lower()

    if symbol == "M":
        words.append("()")

    return "".join(words)


def camel_case(sample: str) -> str:
    splited = sample.split(";")
    operation = splited[0]  # S split and C combine
    symbol = splited[1]  # M method, C class, and V variable
    operable = splited[2]

    return (
        split_words(operable) if operation == "S" else combine_words(operable, symbol)
    )


def split_words_pythonic(content: str) -> str:
    result = []

    for char in content:
        if not char.isalpha():
            continue

        if result and char.isupper():
            result.append(' ')

        result.append(char.lower())

    return "".join(result)


def combine_words_pythonic(content: str, symbol: str) -> str:
    words = [word.title() for word in content.split()]

    if symbol in {'M', 'V'}:
        words[0] = words[0].lower()

    if symbol == 'M':
        words.append('()')

    return "".join(words)


def camel_case_pythonic(sample: str) -> str:
    operation, symbol, content = sample.split(";")

    operations = {
        "S": split_words_pythonic,
        "C": lambda x: combine_words_pythonic(x, symbol),
    }

    return operations[operation](content)


@pytest.mark.parametrize(
    "test_input,test_expected",
    [
        ("S;M;plasticCup()", "plastic cup"),
        ("C;C;coffee machine", "CoffeeMachine"),
        ("C;M;white sheet of paper", "whiteSheetOfPaper()"),
        ("S;C;OrangeHighlighter", "orange highlighter"),
        ("C;V;can of coke", "canOfCoke"),
        ("S;M;sweatTea()", "sweat tea"),
        ("S;V;epsonPrinter", "epson printer"),
        ("C;M;santa claus", "santaClaus()"),
        ("C;C;mirror", "Mirror"),
    ],
)
def test_camel_case(test_input, test_expected):
    assert camel_case(test_input) == test_expected
    assert camel_case_pythonic(test_input) == test_expected
