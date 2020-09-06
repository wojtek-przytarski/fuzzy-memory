from secondtetration.utils.exceptions import InvalidNumberException, RequiredValueMissing

MIN_INPUT_VALUE = -100000
MAX_INPUT_VALUE = 100000


def validate_number(number: str) -> int:
    try:
        number = int(number)
    except ValueError:
        raise InvalidNumberException("Provided value is not an integer")
    except TypeError:
        raise RequiredValueMissing("Please provide a number")
    if number < MIN_INPUT_VALUE or number > MAX_INPUT_VALUE:
        raise InvalidNumberException(f"Provided number is out of range [-{MAX_INPUT_VALUE}, {MAX_INPUT_VALUE}]")
    return number
