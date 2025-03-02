from django.urls import path
from . import views

app_name = "items"
urlpatterns = [
    # return all items
    path('', views.index, name='index'), 

    # filter items using a query parameter
    path('<str:name>', views.get_itemsparam, name='index'),

    # add item
    path('add/<str:id>', views.add_item, name='index'),

    # get item
    path('<int:id>/', views.get_items, name='index'),

    # update item
    path('update/<int:id>/', views.update_item, name='index'),

    # delete item
    path('delete/<int:id>/', views.delete_item, name='index'),
]