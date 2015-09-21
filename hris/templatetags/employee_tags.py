from hris.models import Employee
from hris.models import Role
from django import template
from django.template import resolve_variable
from django.template import resolve_variable, NodeList

register = template.Library()

@register.inclusion_tag('hris/profile-image.html')
def profile_image(employee, css_class="employee-profile-avatar"):
    data = {'css_class': css_class}
    if isinstance(employee, Employee):
        data['success'] = True
        data['image_url'] = employee.image.url
        data['name'] = employee.user.get_full_name()
        return data 
    data['success'] = False
    data['image_url'] =  '/media/hris/employee-image/default-avatar.png'
    return data


@register.tag()
def ifrole(parser, token):
    """ Check to see if the currently logged in user(employee) belongs to one or more roles
    Requires the Django authentication contrib app and middleware.

    Usage: {% ifrole Admins %} ... {% endifrole %}, or
           {% ifrole Admins Clients Programmers Managers %} ... {% else %} ... {% endifrole %}

    """
    try:
        tokensp = token.split_contents()
        roles = []
        roles+=tokensp[1:]
    except ValueError:
        raise template.TemplateSyntaxError("Tag 'ifrole' requires at least 1 argument.")
    
    nodelist_true = parser.parse(('else', 'endifrole'))
    token = parser.next_token()
    
    if token.contents == 'else':
        nodelist_false = parser.parse(('endifrole',))
        parser.delete_first_token()
    else:
        nodelist_false = NodeList()
    
    return GroupCheckNode(roles, nodelist_true, nodelist_false)


class GroupCheckNode(template.Node):

    def __init__(self, roles, nodelist_true, nodelist_false):
        self.roles = roles
        self.nodelist_true = nodelist_true
        self.nodelist_false = nodelist_false

    def render(self, context):
        user = resolve_variable('user', context)
        
        if not user.is_authenticated():
            return self.nodelist_false.render(context)
        
        allowed=False
        for checkrole in self.roles:
            try:
                role = Role.objects.get(code__iexact=checkrole) #hradmin
            except Role.DoesNotExist:
                break
            if role in user.employee.roles.all():
                allowed=True
                break
                
        if allowed:
            return self.nodelist_true.render(context)
        else:
            return self.nodelist_false.render(context)