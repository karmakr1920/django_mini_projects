# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.index, name='home'),
    path('expense-list/', views.expense_list, name='expense-list'),
    path('create/', views.expense_create, name='expense-create'),
    path('<int:pk>/update/', views.expense_update, name='expense-update'),
    path('<int:pk>/delete/', views.expense_delete, name='expense-delete'),
]
