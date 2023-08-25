from rest_framework.serializers import ModelSerializer
from .models import Item, Inventory

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']


class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'quantity', 'item_id', 'player_id']

