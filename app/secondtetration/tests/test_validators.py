import pytest
from rest_framework.exceptions import APIException

from secondtetration.validators import validate_number


@pytest.mark.parametrize(
    "number,expected_message",
    (
        (None, "Please provide a number"),
        ("not a number", "Provided value is not an integer"),
        ("-100001", "Provided number is out of range [-100000, 100000]"),
        ("100001", "Provided number is out of range [-100000, 100000]"),
    ),
)
def test_validate_number_invalid_input(number, expected_message):
    with pytest.raises(APIException) as error:
        validate_number(number)
    assert str(error.value) == expected_message
