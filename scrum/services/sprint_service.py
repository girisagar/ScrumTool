from scrum.models import Sprint

class SprintService(object):
    """docstring for SprintService"""

    @staticmethod
    def all(deleted=False):
        # default returns all undeleted backlogs
        return Sprint.objects.filter(is_deleted=deleted)


    @staticmethod
    def release_backlog_sprints(release_id, deleted=False):
        # default returns all undeleted backlogs
        return Sprint.objects.filter(
            release_backlog__id=release_id,
            is_deleted=deleted
        )