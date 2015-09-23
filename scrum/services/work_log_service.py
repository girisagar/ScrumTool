from scrum.models import WorkLog

class WorkLogService(object):
    """docstring for WorkLogService"""
    
    @staticmethod
    def all(deleted=False):
        # default returns all undeleted userstories
        return WorkLog.objects.filter(
            is_deleted=deleted
        )

    @staticmethod
    def developer_worklogs(employee_id, deleted=False):
        # default returns all undeleted userstories
        return WorkLog.objects.filter(
            employee__id=employee_id,
            log_type='development',
            is_deleted=deleted

        ).order_by('-date')

    @staticmethod
    def tester_worklogs(employee_id, deleted=False):
        # default returns all undeleted userstories
        return WorkLog.objects.filter(
            employee__id=employee_id,
            log_type='test',
            is_deleted=deleted,
        ).order_by('-date')