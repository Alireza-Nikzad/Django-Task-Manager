from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('complete/<int:task_id>/', views.complete_task, name='complete'),
    path('uncomplete/<int:task_id>/', views.uncomplete_task, name='uncomplete'),
    path('edit/<int:task_id>/', views.edit_task, name= 'edit')
]
