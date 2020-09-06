from django.http import JsonResponse, Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SecondTetrationResult
from .tasks import calculate_second_tetration
from .utils.consts import ResultType
from .utils.job_manager import JobManager
from .validators import validate_number


class SecondTetrationView(APIView):
    def post(self, request):
        number = validate_number(request.data.get("number"))
        data = self._second_tetration_response(number)
        return Response(data)

    def _second_tetration_response(self, number: int) -> dict:
        try:
            result = SecondTetrationResult.objects.get_fraction_result(number=number)
            result_type = ResultType.RESULT
        except SecondTetrationResult.DoesNotExist:
            result = JobManager.get_queued_job_id_by_number(number) or calculate_second_tetration.delay(number).id
            result_type = ResultType.JOB_ID
        return {result_type: result}


class JobResultView(APIView):
    def get(self, request, job_id):
        if job := JobManager.get_job_by_id(job_id):
            return JsonResponse({"result": job.return_value})
        else:
            raise Http404()
