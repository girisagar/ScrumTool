from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def employee_role_required(*role_names):
    """Requires employee membership in at least one of the roles passed in."""
    def in_roles(user):
        if user.is_authenticated():
            if bool(user.employee.roles.filter(code__in=role_names)):
                return True
        raise PermissionDenied
    return user_passes_test(in_roles)