from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

# from departments.models import Department, Position


class Employee(AbstractUser):
    """Модель сотрудника."""
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    surname = models.CharField(verbose_name='Отчество', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = None
    password = models.CharField(verbose_name='Пароль', max_length=128)
    photo = models.ImageField(verbose_name='Изображение', upload_to='uploads/')
    position = models.ForeignKey(
        to='departments.Position',
        verbose_name='Должность',
        on_delete=models.SET_NULL,
        related_name='employees',
        null=True
    )
    department = models.ForeignKey(
        to='departments.Department',
        verbose_name='Департамент',
        on_delete=models.SET_NULL,
        related_name='employees',
        null=True
    )
    salary = models.PositiveIntegerField(
        verbose_name='Оклад',
        validators=(
            MinValueValidator(1, 'Должно быть целое число, большее 0'),
        ),
    )
    birthday = models.DateField(verbose_name='День рождения')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('last_name', 'first_name', 'surname')
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'surname', 'last_name', 'department'),
                name='user_in_department'
            ),
        )

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'
