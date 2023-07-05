from api.serializers.users import EmployeeGetListSerializer, EmployeePostPatchSerializer
from api.permissions import IsStaff
from api.filters import EmployeesFilter
from users.models import Employee
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from api.pagination import Pagination
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='get',
    operation_description='GET /users/',
    responses={200: EmployeeGetListSerializer(many=True)}
)
@swagger_auto_schema(
    method='get',
    operation_description='GET /users/{id}/',
    responses={200: EmployeeGetListSerializer(),
               404: 'user not found'}
)
@swagger_auto_schema(
    method='post',
    operation_description='POST /users/',
    responses={200: EmployeePostPatchSerializer()}
)
@swagger_auto_schema(
    method='put',
    operation_description='PUT /users/{id}/',
    responses={200: EmployeePostPatchSerializer(),
               404: 'user not found'}
)
@swagger_auto_schema(
    method='delete',
    operation_description='DELETE /users/{id}/',
    responses={201: 'user deleted', 404: 'user not found'}
)
class UsersViewSet(viewsets.ModelViewSet):
    """Работа с информацией о пользователях."""

    queryset = Employee.objects.select_related(
        'position').select_related('department')
    http_method_names = ('get', 'post', 'put', 'delete')
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
