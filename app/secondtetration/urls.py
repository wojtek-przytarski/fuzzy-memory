from django.urls import path
from . import views

urlpatterns = [
    path("second-tetration/", views.SecondTetrationView.as_view(), name="second-tetration"),
    path("second-tetration/<str:job_id>", views.JobResultView.as_view(), name="get-job-result"),
]
