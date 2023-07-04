from django.contrib import admin

from users.models import Employee


class EmployeeInline(admin.TabularInline):
    model = Employee


@admin.register(Employee)
class RecipeAdmin(admin.ModelAdmin):
    """Представление сотрудников в админ-панели."""

    list_display = (
        'last_name',
        'first_name',
        'surname',
        'username',
        'photo',
        'position',
        'department',
        'salary',
        'is_staff',
    )
    list_filter = ('is_staff', 'department', 'position')
    search_fields = ('last_name',)
