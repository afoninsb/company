from api.serializers.positions import PositionSerializer
from departments.models import Position
from rest_framework import viewsets


class PositionsViewSet(viewsets.ReadOnlyModelViewSet):
    """Список должностей."""
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
