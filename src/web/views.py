from django.views.generic import TemplateView, ListView, DetailView

from .models import Job
from .filters import SearchFilter


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

    def get_queryset(self):
        qs = self.model.objects.all()
        filtered_list = SearchFilter(self.request.GET, queryset=qs)
        return filtered_list.qs
