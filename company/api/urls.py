from django.urls import include, path
from djoser.views import UserViewSet as DjoserUserViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from api.views import DepartmentsViewSet, PositionsViewSet, UsersViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Company API",
      default_version='v1',
      description="API company structure",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'api'

router = SimpleRouter()

router.register('departments', DepartmentsViewSet, basename='departments')
router.register('positions', PositionsViewSet, basename='positions')
router.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('djoser.urls.authtoken')),
    path(
        'users/set_password/',
        DjoserUserViewSet.as_view({'post': 'set_password'})
    ),
    path('', include(router.urls)),
]
