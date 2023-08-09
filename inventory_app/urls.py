from django.urls import path, include
from .views import InventoryView, InventoryAdd, InventoryRemove

urlpatterns = [
    # path('add/', InventoryAdd.as_view()),
    # path('remove/', InventoryRemove.as_view()),
    # path('view/', InventoryView.as_view()),
    path('add/<int:player_id>/', InventoryAdd.as_view()),
    path('remove/<int:player_id>/', InventoryRemove.as_view()),
    path('view/<int:player_id>/', InventoryView.as_view()),
]