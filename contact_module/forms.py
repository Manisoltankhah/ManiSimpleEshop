from django import forms
from .models import ContactUs

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'}),

            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'}),

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'}),

            'message': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'متن پیام',
                    'rows': '5',
                    'id': 'message'})
        }
        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد نمایید',
            },
            'email': {
                'required': 'لطفا ایمیل خود را وارد نمایید',
            },
            'title': {
                'required': 'لطفا عنوان پیام را وارد نمایید',
            },
            'message': {
                'required': 'لطفا متن پیام خود را بنویسید خود را وارد نمایید',
            },
        }

