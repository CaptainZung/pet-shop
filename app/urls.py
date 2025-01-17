from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login/', views.loginPage, name="login"),
    path('search/', views.search, name="search"),
    path('category/', views.category, name="category"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.register, name="register"),
    path('update_item/', views.updateItem, name="update_item"),
    path('detail/', views.detail, name="detail"),
    path('about/', views.about, name="about"),
    path('clear_cart/', views.clear_cart, name="clear_cart"),  # Thêm dòng này
]
