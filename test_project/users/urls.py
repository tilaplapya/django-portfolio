from django.urls import path
from .views import index, get_users, create_user

app_name = "users"
urlpatterns = [
    path('', index, name='index'),
    path('<str:id>', get_users, name='index'),
    path('add/<str:id>', create_user, name='index'),
]