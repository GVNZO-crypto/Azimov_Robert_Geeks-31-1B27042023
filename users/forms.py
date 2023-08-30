from django import forms

#Форма регистрации пользователя

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=32)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
class AuthForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=32)
    password = forms.CharField(widget=forms.PasswordInput())