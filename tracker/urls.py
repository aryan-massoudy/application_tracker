# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('applications/', views.application_list, name='application_list'),
    path('applications/add/', views.application_create, name='application_create'),
    path('applications/<int:pk>/', views.application_detail, name='application_detail'),
    path('applications/<int:pk>/edit/', views.application_update, name='application_update'),
    path('applications/<int:pk>/delete/', views.application_delete, name='application_delete'),
]