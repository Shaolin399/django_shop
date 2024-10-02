# forms.py

from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Phone Number', max_length=20)
    username = forms.CharField(label='Username')  # Додано поле username

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = User.objects.filter(email=email).first()
            if user and not user.check_password(password):
                raise forms.ValidationError('Неправильний email або пароль.')
        return cleaned_data