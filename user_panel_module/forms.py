from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from article_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address', 'about_user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'}),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'}),

            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'}),

            'address': forms.Textarea(attrs={
                    'class': 'form-control',
                    'rows': '3'}),

            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '6'})
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'عکس پروفایل',
            'address': 'آدرس',
            'about_user': 'درباره کاربر',

        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='رمز عبور فعلی',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('رمز عبور و تکرار ان باید شبیه به هم باشند')