from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class Employee(AbstractUser):
    """Модель сотрудника."""

    first_name = models.CharField(verbose_name='Имя', max_length=50)
    surname = models.CharField(verbose_name='Отчество', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    password = models.CharField(verbose_name='Пароль', max_length=128)
    username = models.CharField(max_length=50, unique=True)
    image = models.ImageField(verbose_name='Фото', upload_to='uploads/')
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
        default=13617
    )
    birthday = models.DateField(
        verbose_name='День рождения',
        default='2000-01-01'
        )
    is_staff = models.BooleanField(default=False)

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
