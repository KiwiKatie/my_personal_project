from django.urls import path, include
from .views import InventoryView, InventoryAdd, InventoryRemove

urlpatterns = [
    path('add/', InventoryAdd.as_view()),
    path('remove/', InventoryRemove.as_view()),
    path('view/', InventoryView.as_view()),
]