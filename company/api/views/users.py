from api.serializers.users import EmployeeGetListSerializer, EmployeePostPatchSerializer
from api.permissions import IsStaff
from api.filters import EmployeesFilter
from users.models import Employee
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from api.pagination import Pagination


class UsersViewSet(viewsets.ModelViewSet):
    """Работа с информацией о пользователях."""
    queryset = Employee.objects.select_related(
        'position').select_related('department')
    http_method_names = ('get', 'post', 'patch', 'delete')
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, )
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
