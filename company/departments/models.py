from django.db import models


class Position(models.Model):
    """Модель должности."""
    name = models.CharField(
        verbose_name='Должность',
        max_length=100
    )

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Department(models.Model):
    """Модель департамента."""
    name = models.CharField(
        verbose_name='Департамент',
        max_length=100
    )
    director = models.ForeignKey(
        to='users.Employee',
        verbose_name='Директор',
        on_delete=models.SET_NULL,
        related_name='dir_department',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return self.name
