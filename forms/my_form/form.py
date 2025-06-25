from django import forms
import re

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=50,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'First name...'}),
        error_messages={
            'required' : 'This is a required field',
            'max_length' : 'Name should not exceed more than 50 words',
            'min_length' : 'minimum length should be 2 letters'
        }
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=50,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Last name...'}),
        error_messages={
            'required' : 'This is a required field',
            'max_length' : 'Name should not exceed more than 50 words',
            'min_length' : 'minimum length should be 2 letters'
        }
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder':'example@gmail.com'}),
        error_messages={
            'required' : 'This is a required field',
            'invalid' : 'Enter a valid email address.'        
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Password'}),
        required=True,
        error_messages={
            'required' : 'This is a required field'
        }
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Repeat password'}),
        required=True,
        error_messages={
            'required' : 'This a required field',
            'invalid' : 'Password does not match'
        }
    )

    def clean_password(self):
        data = self.cleaned_data['password']
        errors = []

        if not any(char.isdigit() for char in data):
            errors.append('Password must contain at least one digit.')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', data):
            errors.append('Password must contain at least one special character.')

        if errors:
            raise forms.ValidationError(errors)

        return data

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        confirm_pwd = cleaned_data.get('confirm_password')

        if pwd and confirm_pwd and pwd != confirm_pwd:
            self.add_error('confirm_password', 'Passwords do not match.')
        
class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder':'example@gmail.com'}),
        error_messages={
            'required' : 'This is a required field',
            'invalid' : 'Enter a valid email address.'        
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Password'}),
        required=True,
        error_messages={
            'required' : 'This is a required field'
        }
    )