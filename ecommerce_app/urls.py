from django.urls import path
from ecommerce_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('buyer_dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
]
