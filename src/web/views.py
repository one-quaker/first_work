from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

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

    def get_queryset(self):
        qs = self.model.objects.all()
        q = self.request.GET.get('name', '')

        try:
            job_type = int(self.request.GET.get('job_type'))
        except:
            job_type = None

        if job_type in (Job.JOB_DEFAULT, Job.JOB_VOLUNTEER, Job.JOB_INTERNSHIP):
            qs = self.model.objects.filter(job_type=job_type)
        elif q:
            qs = self.model.objects.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q)
            )

        return qs
