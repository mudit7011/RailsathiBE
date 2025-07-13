from django.urls import path
from .views import item_list

urlpatterns = [
    path('', item_list, name='item-list'),
    path('items/', item_list, name='item-list'),
]