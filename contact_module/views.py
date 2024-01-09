from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from site_module.models import SiteSetting
from .forms import ContactUsModelForm
from django.views.generic.edit import FormView, CreateView
from .models import ContactUs, UserProfile

class ContactUsView(CreateView):
    model = ContactUs
    # fields = ['']
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting

        return context


    # def form_valid(self, form):
    #     form.save()
    #     return super(ContactUsView, self).form_valid(form)


    # def get(self,request):
    #     contact_form = ContactUsModelForm()
    #     return render(request, 'contact_module/contact_us_page.html', {
    #         'contact_form': contact_form
    #     })
    # def post(self,request):
    #     contact_form = ContactUsModelForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.save()
    #         return redirect('home_page')
    #     return render(request, 'contact_module/contact_us_page.html', {
    #         'contact_form': contact_form
    #     })

class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile/'

class ProfilesView(ListView):
    model = UserProfile
    template_name = 'contact_module/profile_list_page.html'
    context_object_name = 'profiles'