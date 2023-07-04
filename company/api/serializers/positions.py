from rest_framework import serializers

from departments.models import Position


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор модели Position."""

    class Meta:
        model = Position
        fields = '__all__'
