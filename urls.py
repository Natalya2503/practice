from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tasks/<int:task_id>/', views.details),
    
]