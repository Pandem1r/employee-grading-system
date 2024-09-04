from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Grading, Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class GradingForm(forms.ModelForm):
    class Meta:
        model = Grading
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Используем select_related для получения данных профиля пользователя
        self.fields['user'].queryset = User.objects.filter(profile__isnull=False).select_related('profile')
