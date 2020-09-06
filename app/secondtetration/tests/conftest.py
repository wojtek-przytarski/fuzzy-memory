import pytest

from secondtetration.models import SecondTetrationResult

from secondtetration.utils.fraction_result import FractionResult


@pytest.fixture
def fraction_result_for_11():
    return FractionResult("285311670611")


@pytest.fixture
def fraction_result_for_minus_11():
    return FractionResult("-1", "285311670611")


@pytest.fixture
def results_db(db, fraction_result_for_11):
    SecondTetrationResult.objects.create(
        number=11,
        result=fraction_result_for_11["numerator"],
    )
    yield results_db


@pytest.fixture
def expected_new_job_response():
    return {"job_id": "job-id-1"}
