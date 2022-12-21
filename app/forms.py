from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username','password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=4,widget=forms.PasswordInput)

    def clean_password(self):
        data = self.cleaned_data['password']
        if data=='wrongpassword':
            raise ValidationError("Error password")
        return data

class RegistrationForm(forms.ModelForm):
    password_check = forms.CharField(min_length=4,widget=forms.PasswordInput)
    password = forms.CharField(min_length=4,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username','first_name','last_name','password']

    def clean(self):
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_check']

        if password_1 != password_2:
            raise ValidationError("Password do not match")
        return self.cleaned_data

    def save(self):
        self.cleaned_data.pop('password_check')
        return User.objects.create_user(**self.cleaned_data)
class AskForm(forms.ModelForm):
    title = forms.CharField(min_length=4,max_length=20, widget=forms.CharField)
    text = forms.CharField(widget=forms.CharField)
    tags = forms.CharField(min_length=4,max_length=20, widget=forms.CharField)

