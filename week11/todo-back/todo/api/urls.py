from django.conf import settings
from django.urls import path
from api import views

urlpatterns = [
    path('api/task_lists/', views.list_lists, name = "lists"),
    path('api/task_lists/<int:list_id>/', views.list_detail, name = "list_detail"),
    path('api/task_lists/<int:list_id>/tasks/<int:task_id>/', views.task_detail,name='task_detail')
]