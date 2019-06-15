import django_filters
from .models import Job


class SearchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = [
            'name',
            'description',
            'city',
            'job_type',
        ]
