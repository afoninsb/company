from rest_framework import serializers

from users.models import Employee


class DirectorSerializer(serializers.ModelSerializer):
    """Сериализатор модели Employee для директора."""

    class Meta:
        model = Employee
        fields = (
            'id', 'last_name', 'first_name', 'surname', 'photo',
        )
