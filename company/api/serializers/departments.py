from api.serializers.users import DirectorSerializer
from rest_framework import serializers
from django.db.models import Sum
from departments.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Department."""

    director = DirectorSerializer(read_only=True)

    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ('name', 'director')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['count_employees'] = instance.employees.count()
        obj = instance.employees.aggregate(total_salary=Sum('salary'))
        representation['total_salary'] = obj.total_salary
        return representation


class DepartmentUserSerializer(serializers.ModelSerializer):
    """Сериализатор модели Department для сотрудника."""

    class Meta:
        model = Department
        fields = ('id', 'name')
        read_only_fields = ('name', )
