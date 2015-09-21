from scrum.models import WorkLog

class WorkLogService(object):
    """docstring for WorkLogService"""
    
    @staticmethod
    def all(deleted=False):
        # default returns all undeleted userstories
        return WorkLog.objects.filter(
            is_deleted=deleted
        )