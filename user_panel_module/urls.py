from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
urlpatterns = [
    path('', login_required(views.UserPanelDashboardPage.as_view()), name='user_panel_dashboard'),
    path('change-password', login_required(views.ChangePasswordPage.as_view()), name='change_password_page'),
    path('edit-profile', login_required(views.EditUserProfilePage.as_view()), name='edit_profile_page'),
    path('user-cart', views.user_cart, name='user-cart'),
    path('remove-order-detail', views.remove_order_detail, name='remove-cart-detail-ajax'),
    path('change-order-detail', views.change_order_detail_count, name='change_order_detail_count'),
]