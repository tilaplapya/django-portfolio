from django.urls import path 
from .views import index 
from .views import portfolio

app_name = "portfolio"
urlpatterns = [  
    path( 'portfolio/', portfolio, name='portfolio'),
] 