import pytest
from presidio_anonymizer.operators import Initial

def test_correct_name():
    assert Initial().operator_name() == "initial"

@pytest.mark.parametrize(
    "input_text, expected_initials",
    [
        # Standard case
        ("John Smith", "J. S."),
        # New case: Extra whitespaces and leading/trailing spaces
        ("      Eastern     Michigan    University ", "E. M. U."),
    ],
)
def test_given_value_for_initial(input_text, expected_initials):
    text = Initial().operate(input_text)
    assert text == expected_initials