from django.urls import path 
from .views import index 
from .views import portfolio
from .views import dashboard

app_name = "portfolio"
urlpatterns = [  
    path( 'portfolio/', portfolio, name='portfolio'),
    path( '', index, name='index'),
    path( 'dashboard/', dashboard, name='dashboard'),
] 