from django.db import transaction
from django_rq import job

from .models import SecondTetrationResult
from .utils.fraction_result import FractionResult


@job
@transaction.atomic
def calculate_second_tetration(number: int) -> FractionResult:
    absolute = abs(number)
    obj, created = SecondTetrationResult.objects.select_for_update().get_or_create(number=absolute)
    if created:
        obj.result = str(second_tetration(absolute))
        obj.save()
    return FractionResult.parse_from_number_and_result(number, obj.result)


def second_tetration(number: int) -> int:
    return number ** number
