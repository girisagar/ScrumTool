from scrum.models import ProductBacklog

class ProductBacklogService(object):
    """docstring for ProductBacklogService"""

    @staticmethod
    def all(deleted=False):
        # default returns all undeleted backlogs
        return ProductBacklog.objects.filter(is_deleted=deleted)