from typing import Optional

import django_rq
from django_rq.jobs import Job
from django_rq.queues import Queue


class JobManager:
    @staticmethod
    def get_job_by_id(job_id: str) -> Optional[Job]:
        """
        Returns Job for given id if exists
        """
        redis_connection = django_rq.get_connection()
        try:
            return Job.fetch(job_id, redis_connection)
        except Exception:
            return None

    @staticmethod
    def get_queued_job_id_by_number(number: int) -> Optional[str]:
        """
        Returns job_id when job for the same number exists
        """
        redis_connection = django_rq.get_connection()
        queue = Queue(connection=redis_connection)
        job_ids = queue.started_job_registry.get_job_ids() + queue.scheduled_job_registry.get_job_ids()
        for job_id in job_ids:
            job = JobManager.get_job_by_id(job_id)
            if number in job.args:
                return job.id
