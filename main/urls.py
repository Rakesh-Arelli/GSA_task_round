# main/urls.py
from django.urls import path
from .views import RegisterView, LoginView, TaskCreateView, TaskListView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('users/', UserListView.as_view(), name='user-list'),
]
