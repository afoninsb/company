from api.serializers.positions import PositionSerializer
from departments.models import Position
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='get',
    operation_description='GET /positions/',
    responses={200: PositionSerializer(many=True)}
)
@swagger_auto_schema(
    method='get',
    operation_description='GET /positions/{id}/',
    responses={200: PositionSerializer()}
)
class PositionsViewSet(viewsets.ReadOnlyModelViewSet):
    """Список должностей."""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
