from api.serializers.departments import DepartmentSerializer
from departments.models import Department
from rest_framework import viewsets


class DepartmentsViewSet(viewsets.ReadOnlyModelViewSet):
    """Список департаментов."""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
