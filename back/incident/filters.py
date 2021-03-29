import django_filters

from .models import Incident


class IncidentFilter(django_filters.FilterSet):
    date_month = django_filters.NumberFilter(field_name='date__month', lookup_expr='exact')

    class Meta:
        model = Incident
        fields = ['date']
