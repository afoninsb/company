from api.serializers.departments import DepartmentSerializer
from departments.models import Department
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='get',
    operation_description='GET /departments/',
    responses={200: DepartmentSerializer(many=True)}
)
@swagger_auto_schema(
    method='get',
    operation_description='GET /departments/{id}/',
    responses={200: DepartmentSerializer()}
)
class DepartmentsViewSet(viewsets.ReadOnlyModelViewSet):
    """Список департаментов."""

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
