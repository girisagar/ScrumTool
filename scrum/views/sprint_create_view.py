from django.views.generic.edit import CreateView
from scrum.models import Sprint, ReleaseBacklog
from django.contrib import messages
from django.utils.decorators import method_decorator
from hris.decorators import employee_role_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.http import Http404

class SprintCreateView(CreateView):
    model = Sprint
    fields = ('name', )

    @method_decorator(employee_role_required("scrum_master"))
    def dispatch(self,  *args, **kwargs):
        self.release_id = kwargs.get('release_id',None)
        return super(SprintCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.release_backlog_id = self.release_id
        form.instance.created_by = self.request.user.employee
        form.instance.updated_by = self.request.user.employee
        return super(SprintCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # import pdb;pdb.set_trace()
        context = super(SprintCreateView, self).get_context_data(**kwargs)
        context['release_backlog'] = self.get_release_object()
        return context
        
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, \
            'New Sprint successfully added to {0}'.format(
                self.get_release_object().name
            )
        )        
        return reverse_lazy(
            'scrum_product_backlog_detail',
            args = [self.get_release_object().product_backlog.id]
        )

    def get_release_object(self):
        release_backlog = None
        try:
            self.release_backlog = ReleaseBacklog.objects.get(id=self.release_id)
        except Exception, e:
            raise Http404
        return self.release_backlog