from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidNumberException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class RequiredValueMissing(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
