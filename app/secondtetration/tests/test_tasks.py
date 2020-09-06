import pytest

from secondtetration.tasks import calculate_second_tetration
from secondtetration.utils.fraction_result import FractionResult


@pytest.mark.parametrize(
    "number,expected_result",
    (
        (5, FractionResult("3125")),
        (-5, FractionResult("-1", "3125")),
        (4, FractionResult("256")),
        (-4, FractionResult("1", "256")),
        (0, FractionResult("1")),
    ),
)
def test_calculate_second_tetration_for_different_numbers(db, number, expected_result):
    result = calculate_second_tetration(number)
    assert result == expected_result


def test_calculate_second_tetration_for_the_same_number_calculates_once(db, mocker):
    function_mock = mocker.patch("secondtetration.tasks.second_tetration")
    number = 4
    calculate_second_tetration(number)
    calculate_second_tetration(number)
    function_mock.assert_called_once_with(number)


def test_calculate_second_tetration_for_the_opposite_number_calculates_once(db, mocker):
    function_mock = mocker.patch("secondtetration.tasks.second_tetration")
    number = 4
    calculate_second_tetration(number)
    calculate_second_tetration(-number)
    function_mock.assert_called_once_with(number)
