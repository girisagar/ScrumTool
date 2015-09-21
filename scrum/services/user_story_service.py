from scrum.models import UserStory

class UserStoryService(object):
    """docstring for UserStoryService"""

    @staticmethod
    def all(deleted=False):
        # default returns all undeleted userstories
        return UserStory.objects.filter(
            is_deleted=deleted
        )

    @staticmethod
    def product_backlog_stories(product_id, deleted=False):
        # default returns all undeleted userstories where release_backlog=null, sprint=null
        return UserStory.objects.filter(
            product_backlog__id=product_id,
            release_backlog__isnull=True,
            sprint__isnull=True,
            is_deleted=deleted
        )

    @staticmethod
    def release_backlog_stories(release_id, deleted=False):
        # default returns all undeleted userstories where sprint=null
        return UserStory.objects.filter(
            release_backlog__id=release_id,
            is_deleted=deleted,
            sprint__isnull=True
        )

    @staticmethod
    def sprint_backlog_stories(sprint_id, deleted=False):
        # default returns all undeleted userstories where
        return UserStory.objects.filter(
            sprint__id=sprint_id,
            is_deleted=deleted
        )