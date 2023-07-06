from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.filters import EmployeesFilter
from api.pagination import Pagination
from api.permissions import IsStaff
from api.serializers import (DepartmentSerializer, EmployeeGetListSerializer,
                             EmployeePostPatchSerializer, PositionSerializer)
from departments.models import Department, Position
from users.models import Employee


class UsersViewSet(viewsets.ModelViewSet):
    """Работа с информацией о пользователях."""

    queryset = Employee.objects.select_related(
        'position').select_related('department')
    http_method_names = ('get', 'post', 'put', 'delete')
    pagination_class = Pagination
    filterset_class = EmployeesFilter

    def get_serializer_class(self):
        """Выбор сериализатора."""

        if self.action in ('retrieve', 'list'):
            return EmployeeGetListSerializer
        if self.action in ('create', 'update'):
            return EmployeePostPatchSerializer

    def get_permissions(self):
        """Права доступа для запросов."""

        if self.action in ('create', 'update', 'destroy'):
            self.permission_classes = (IsStaff, )
        else:
            self.permission_classes = (IsAuthenticated, )
        return super().get_permissions()


class DepartmentsViewSet(viewsets.ReadOnlyModelViewSet):
    """Список департаментов."""

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny, )


class PositionsViewSet(viewsets.ReadOnlyModelViewSet):
    """Список должностей."""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (AllowAny, )
