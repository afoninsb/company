from django.contrib import admin
from django.db.models import Count, Sum

from departments.models import Department, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """Представление должностей в админ-панели."""

    list_display = ('id', 'name', )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Представление департаментов в админ-панели."""

    list_display = ('id', 'name', 'director')
    readonly_fields = ('count_employee', 'total_salary')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            _count_employee=Count('employees'),
            _total_salary=Sum('employees__salary')
        )

    def count_employee(self, obj):
        """Количество сотрудников в департаменте."""

        return obj._count_employee

    def total_salary(self, obj):
        """Общий оклад по департаменту."""

        return obj._total_salary

    count_employee.short_description = "Количество сотрудников"
    total_salary.short_description = "Общий оклад по департаменту"
