from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
