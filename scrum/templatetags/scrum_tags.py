from django import template
from django.template import resolve_variable
from scrum.services import UserStoryService

register = template.Library()

@register.inclusion_tag('templatetags/release_stories.html')
def load_release_stories(release, user):
    release_stories = UserStoryService.release_backlog_stories(release.id)
    data = {
        'release_stories' : release_stories,
        'user' : user
    }
    return data