from django import template
from django.template import resolve_variable
from django.template import resolve_variable, NodeList

register = template.Library()

@register.simple_tag
def get_sprints(dict_, key):
	return [str(i) for i in dict_[key]["sprints"]]