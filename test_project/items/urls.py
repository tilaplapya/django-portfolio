from django.urls import path
from . import views

app_name = "items"
urlpatterns = [
    # Return all items
    path('', views.index, name='get_all_items'),
    
    # Get a single item
    path('<int:item_id>/', views.get_item, name='get_item'),
    
    # Add a new item
    path('add/', views.add_item, name='add_item'),
    
    # Update an item
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    
    # Delete an item
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]