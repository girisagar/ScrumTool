from hris.models import Employee
from django import template

register = template.Library()

@register.inclusion_tag('employee/profile-image.html')
def profile_image(employee, css_class="employee-profile-avatar"):
	data = {'css_class': css_class}
	if isinstance(employee, Employee):
		data['success'] = True
		data['image_url'] = employee.image.url
		data['name'] = employee.user.get_full_name()
		return data	
	data['success'] = False
	data['image_url'] =	 '/media/hris/employee-image/default-avatar.png'
	return data