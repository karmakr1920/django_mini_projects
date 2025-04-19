from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Handles both create and edit
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
