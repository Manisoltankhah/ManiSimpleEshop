from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product-categories-list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product-brand-list'),
    path('product-favorite', views.AddProductFavorite.as_view(), name='product-favorite'),
    path('add_product_comment', views.add_product_comment, name='add_product_comment'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name="product_detail"),
]
