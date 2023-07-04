from django.contrib import admin
from django.db.models import Count
from users.admin import EmployeeInline

from departments.models import Department, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """Представление должностей в админ-панели."""

    list_display = ('name', )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Представление департаментов в админ-панели."""

    list_display = ('name', 'director')
    # inlines = (EmployeeInline,)
    readonly_fields = ('count_employee',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            _count_employee=Count('employees'))

    def count_employee(self, obj):
        """Количество сотрудников в департаменте."""
        return obj._count_employee

    count_employee.short_description = "Количество сотрудников"
