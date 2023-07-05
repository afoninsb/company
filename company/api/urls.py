from django.urls import include, path
from api.views.departments import DepartmentsViewSet
from api.views.positions import PositionsViewSet
from api.views.users import UsersViewSet
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.routers import SimpleRouter


app_name = 'api'

router = SimpleRouter()

router.register('departments', DepartmentsViewSet, basename='departments')
router.register('positions', PositionsViewSet, basename='positions')
router.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path(
        'users/set_password/',
        DjoserUserViewSet.as_view({'post': 'set_password'})
    ),
    path('', include(router.urls)),
]
