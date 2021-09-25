from django.urls import path
from .views import register_task, task_lisk,edit_task

urlpatterns = [
    path('register',register_task,name='register_task'),
    path('list/',task_lisk,name='task_list'),
    path('edit/<int:id>/',edit_task,name='edit_task')
]
