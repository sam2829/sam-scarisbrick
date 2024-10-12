import django_filters
from .models import Project


class ProjectFilter(django_filters.FilterSet):
    technology_name = django_filters.CharFilter(field_name='technologies__name', lookup_expr='iexact')

    class Meta:
        model = Project
        fields = ['technology_name']