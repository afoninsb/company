from django.contrib import admin
from django import forms
from users.models import Employee
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Подтвердите пароль", widget=forms.PasswordInput
    )

    class Meta:
        model = Employee
        fields = (
            'id', 'last_name', 'first_name', 'surname', 'username', 'password',
            'image', 'position', 'department', 'salary', 'birthday',
            'is_staff',
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Employee
        fields = (
            'id', 'last_name', 'first_name', 'surname', 'username',
            'password', 'image', 'position', 'department', 'salary',
            'birthday', 'is_staff'
        )


@admin.register(Employee)
class EmploeeAdmin(BaseUserAdmin):
    """Представление сотрудников в админ-панели."""

    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        'id',
        'last_name',
        'first_name',
        'surname',
        'username',
        'image',
        'position',
        'department',
        'salary',
        'is_staff',
    )
    fieldsets = [
        ("ФИО", {"fields": ["last_name", "first_name", "surname"]}),
        ("ЛОГИН", {"fields": ["username", "password"]}),
        ("ИНФО", {"fields":
                  ["image", "position", "department", "salary", "is_staff"]}),
    ]
    list_filter = ('is_staff', 'department', 'position')
    search_fields = ('last_name',)
