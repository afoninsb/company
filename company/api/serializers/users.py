from api.serializers.departments import DepartmentUserSerializer
from rest_framework import serializers
import base64
from uuid import uuid1
from django.conf import settings
from django.core.files.base import ContentFile
from users.models import Employee
from api.serializers.positions import PositionSerializer


class EmployeeGetListSerializer(serializers.ModelSerializer):
    """Сериализатор модели Employee - GET, LIST."""

    photo = serializers.ImageField(use_url=True)
    position = PositionSerializer()
    department = DepartmentUserSerializer()

    class Meta:
        model = Employee
        fields = (
            'id', 'last_name', 'first_name', 'surname', 'photo',
            'position', 'department', 'salary', 'birthday', 'is_staff'
        )


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(
                base64.b64decode(imgstr), name=f'{uuid1()}.{ext}')
        return super().to_internal_value(data)


class EmployeePostPatchSerializer(serializers.ModelSerializer):
    """Сериализатор модели Employee - POST, PATCH."""

    photo = Base64ImageField()
    position = serializers.PrimaryKeyRelatedField()
    department = serializers.PrimaryKeyRelatedField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = (
            'last_name', 'first_name', 'surname', 'username', 'password',
            'photo', 'position', 'department', 'salary', 'birthday', 'is_staff'
        )


class DirectorSerializer(serializers.ModelSerializer):
    """Сериализатор модели Employee для директора."""

    photo = serializers.ImageField(use_url=True)

    class Meta:
        model = Employee
        fields = ('last_name', 'first_name', 'surname', 'photo')
        read_only_fields = ('last_name', 'first_name', 'surname', 'photo')
