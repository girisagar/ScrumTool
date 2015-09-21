from scrum.models import ReleaseBacklog

class ReleaseBacklogService(object):
    """docstring for ReleaseBacklogService"""

    @staticmethod
    def all(deleted=False):
        # default returns all undeleted backlogs
        return ReleaseBacklog.objects.filter(is_deleted=deleted)


    @staticmethod
    def product_backlog_releases(product_id, deleted=False):
        # default returns all undeleted backlogs
        return ReleaseBacklog.objects.filter(
            product_backlog_id=product_id,
            is_deleted=deleted
        )