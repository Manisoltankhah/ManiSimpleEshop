from django.urls import path
from . import views

urlpatterns = [
    # path('', views.contact_us_page, name='contact-us-page'),
    path('', views.ContactUsView.as_view(), name='contact-us-page'),
    path('create-profile/', views.CreateProfileView.as_view(), name='create-profile-page'),
    path('profiles/', views.ProfilesView.as_view(), name='profile-list-page'),
]