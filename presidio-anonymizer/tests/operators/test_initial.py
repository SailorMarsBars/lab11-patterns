import pytest
from presidio_anonymizer.operators import Initial

def test_correct_name():
    assert Initial().operator_name() == "initial"

@pytest.mark.parametrize(
    "input_text, expected_initials",
    [
        # original case
        ("John Smith", "J. S."),
        # whitespace case
        ("      Eastern     Michigan    University ", "E. M. U."),
        # New "prefix preservation" cases
        ("@abc", "@A."),
        ("@843A", "@8."),
        ("--**abc", "--**A."),
        # Combined case (sentence with prefixes)
        ("#1 priority", "#1. P."),
    ],
)
def test_given_value_for_initial(input_text, expected_initials):
    text = Initial().operate(input_text)
    assert text == expected_initials