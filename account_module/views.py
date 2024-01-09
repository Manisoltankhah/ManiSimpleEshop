from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import User
from account_module.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout
from django.core.mail import EmailMessage


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        # print(f'random string: {get_random_string(6)}')
        context = {
            "register_form": register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل یا نام کاربری وارد شده قبلا استفاده شده')
            else:
                new_user = User(email=user_email, email_active_code=get_random_string(6), is_active=False, username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                email_to_user = EmailMessage('فعال سازی حساب کاربری', f'''http://127.0.0.1:8080/activate-account/{new_user.email_active_code}''', to=[f'{new_user.email}'])
                email_to_user.send()
                return redirect(reverse('login_page'))

        context = {
              "register_form": register_form
        }
        return render(request, 'account_module/register.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.email_active_code = get_random_string(6)
                user.is_active = True
                user.save()
                return redirect(reverse('login_page'))
            else:
                pass
        raise Http404


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        context = {
            "login_form": login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری فعال نشده')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))

        context = {
             "login_form": login_form
        }
        return render(request, 'account_module/login.html', context)


class ForgotPasswordView(View):

    def get(self, request):
        forgot_password_form = ForgotPasswordForm()
        context = {
            'forgot_password_form': forgot_password_form
        }
        return render(request, 'account_module/forget_password.html', context)

    def post(self, request):
        forgot_password_form = ForgotPasswordForm(request.POST)
        if forgot_password_form.is_valid():
            user_email = forgot_password_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                pass

        context = {
            'forgot_password_form': forgot_password_form
        }
        return render(request, 'account_module/forget_password.html', context)


class ResetPasswordView(View):

    def get(self, request, active_code):
        user = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))
        reset_pass_form = ResetPasswordForm()
        context = {'reset_pass_form': reset_pass_form,
                   'user': user
                   }
        return render(request, 'account_module/reset_password.html', context)

    def post(self, request, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))
            user_new_password = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_password)
            user.email_active_code = get_random_string(6)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'account_module/reset_password.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))
