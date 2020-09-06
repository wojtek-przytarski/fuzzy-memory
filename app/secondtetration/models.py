from django.db import models

from secondtetration.utils.fraction_result import FractionResult


class SecondTetrationResultQuerySet(models.QuerySet):
    """
    Override default queryset to handle also negative integers and return a FractionResult dict
    """

    def get_fraction_result(self, number: int) -> FractionResult:
        result = self.get(number=abs(number)).result
        return FractionResult.parse_from_number_and_result(number, result)


class SecondTetrationResultManager(models.Manager.from_queryset(SecondTetrationResultQuerySet)):
    """
    Manager for the SecondTetrationResultQuerySet
    """


class SecondTetrationResult(models.Model):
    number = models.IntegerField(unique=True)
    result = models.CharField(max_length=500001)

    objects = SecondTetrationResultManager()

    def __str__(self):
        return f"<SecondTetrationResult {self.number}={self.result}>"
