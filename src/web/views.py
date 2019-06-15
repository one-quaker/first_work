from django.views.generic import TemplateView, ListView, DetailView

from .models import Job


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


class JobListView(ListView):
    template_name = 'job_list.html'
    model = Job

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
