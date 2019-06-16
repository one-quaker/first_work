from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView, JobListView, JobDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
    re_path('^job/(?P<slug>[0-9A-Za-z\-]+)$', JobDetailView.as_view(), name='job-detail-page'),
    path('job-list/', JobListView.as_view(), name='job-list-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
