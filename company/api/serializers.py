import base64
from uuid import uuid1

from django.core.files.base import ContentFile
from django.db.models import Sum
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from departments.models import Department, Position
from users.models import Employee


class DirectorSerializer(serializers.ModelSerializer):
    """Сериализатор модели Employee для директора."""

    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Employee
        fields = ('last_name', 'first_name', 'surname', 'image')
        read_only_fields = ('last_name', 'first_name', 'surname', 'image')


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
        representation['total_salary'] = obj['total_salary']
        return representation


class DepartmentUserSerializer(serializers.ModelSerializer):
    """Сериализатор модели Department для сотрудника."""

    class Meta:
        model = Department
        fields = ('id', 'name')
        read_only_fields = ('name', )


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор модели Position."""

    class Meta:
        model = Position
        fields = '__all__'


class EmployeeGetListSerializer(serializers.ModelSerializer):
    """Сериализатор модели Employee - GET, LIST."""

    image = serializers.ImageField(use_url=True)
    position = PositionSerializer()
    department = DepartmentUserSerializer()

    class Meta:
        model = Employee
        fields = (
            'id', 'last_name', 'first_name', 'surname', 'username', 'image',
            'position', 'department', 'salary', 'birthday', 'is_staff',
        )


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(
                base64.b64decode(imgstr), name=f'{uuid1()}.{ext}')
        return super().to_internal_value(data)


class EmployeePostPatchSerializer(UserCreateSerializer):
    """Сериализатор модели Employee - POST, PATCH."""

    position = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all())
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all())
    image = Base64ImageField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = (
            'id', 'last_name', 'first_name', 'surname', 'image',
            'position', 'department', 'salary', 'birthday', 'is_staff',
            'username', 'password',
        )
