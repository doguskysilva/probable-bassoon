import pytest


def split_words(operable: str) -> str:
    output = ""

    for char in operable:
        if char.islower():
            output += char
        elif char.isalpha():
            if output == "":
                output += char.lower()
            else:
                output += " " + char.lower()

    return output

def combine_words(operable: str, symbol: str) -> str:
    output = ""
    words = operable.title().split(" ")
    if symbol == "C":
        output = "".join(words)
    elif symbol == "M":
        words[0] = words[0].lower()
        words.append("()")
        output = "".join(words)
    else:
        words[0] = words[0].lower()
        output = "".join(words)

    return output

def camel_case(sample_input: str) -> str:
    splited_input = sample_input.split(";")
    operation = splited_input[0] # S split and C combine
    symbol = splited_input[1] # M method, C class, and V variable
    operable = splited_input[2]

    return split_words(operable) if operation == "S" else combine_words(operable, symbol)
        


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
        ("C;C;mirror", "Mirror")

    ],
)
def test_camel_case(test_input, test_expected):
    assert camel_case(test_input) == test_expected
