from django.views.generic.edit import CreateView
from scrum.models import ReleaseBacklog
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class ReleaseBacklogCreateView(CreateView):
    model = ReleaseBacklog
    fields = ('name',)

    # @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(ReleaseBacklogCreateView, self).dispatch(*args, **kwargs)