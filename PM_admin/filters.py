import django_filters
from PM.models import Project


class ProjectFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter()

    class Meta:
        model = Project
        fields = ['id', 'Project_leader', 'Current_status', 'Project_type', 'Project_name']
        order_by_field = ['id', 'Project_leader']