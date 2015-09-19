from django.views.generic.edit import UpdateView
from scrum.models import Sprint
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required

class SprintUpdateView(UpdateView):
    model = Sprint
    fields = ('name',)

    # @method_decorator(employee_role_required("product_owner"))
    def dispatch(self, *args, **kwargs):
        return super(SprintUpdateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user.employee
        return super(SprintUpdateView, self).form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super(SprintUpdateView, self).get_context_data(**kwargs)
        context['release_backlog'] = self.get_object().release_backlog
        return context

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, \
            'Sprint successfully Updated'
        )       
        success_url = reverse_lazy('scrum_product_backlog',
            args = [self.get_object().release_backlog.product_backlog.id]
        )
        return success_url