from django_filters import rest_framework as filters

from users.models import Employee


class EmployeesFilter(filters.FilterSet):
    """Фильтры сотрудников."""

    last_name = filters.CharFilter()
    department = filters.NumberFilter()

    class Meta:
        model = Employee
        fields = ('last_name', 'department')
