from unittest.mock import Mock

from django.urls import reverse
from rest_framework import status


def test_second_tetration_view_for_already_calculated(results_db, client, fraction_result_for_11):
    url = reverse("second-tetration")
    response = client.post(url, {"number": 11})
    assert response.json() == {"result": fraction_result_for_11}


def test_second_tetration_view_for_already_calculated_opposite(results_db, client, fraction_result_for_minus_11):
    url = reverse("second-tetration")
    response = client.post(url, {"number": -11})
    assert response.json() == {"result": fraction_result_for_minus_11}


def test_second_tetration_view_for_new_value(db, client, mocker, expected_new_job_response):
    mocker.patch(
        "secondtetration.utils.job_manager.JobManager.get_queued_job_id_by_number",
        return_value="job-id-1",
    )
    url = reverse("second-tetration")
    response = client.post(url, {"number": 11111})
    assert response.json() == expected_new_job_response


def test_job_result_view_for_non_existent_id(client, mocker):
    mocker.patch(
        "secondtetration.utils.job_manager.JobManager.get_job_by_id",
        return_value=None,
    )
    url = reverse("get-job-result", args=("job-id-1",))
    response = client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_job_result_view_for_finished_job(client, mocker, fraction_result_for_11):
    mocker.patch(
        "secondtetration.utils.job_manager.JobManager.get_job_by_id",
        return_value=Mock(return_value=fraction_result_for_11),
    )
    url = reverse("get-job-result", args=("job-id-1",))
    response = client.get(url)
    assert response.json() == {"result": fraction_result_for_11}
