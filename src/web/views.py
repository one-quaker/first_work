from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['project_title'] = 'First work'
        return ctx
