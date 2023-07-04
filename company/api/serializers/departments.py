from rest_framework import serializers

from departments.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Department."""

    class Meta:
        model = Department
        fields = '__all__'
