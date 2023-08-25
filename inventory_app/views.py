from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Item, Inventory
from player_app.models import PlayerTraits
from .serializers import InventorySerializer


class InventoryView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        try:
            player = PlayerTraits.objects.get(user=request.user)
            inventory_items=Inventory.objects.filter(player=player)
            serializer = InventorySerializer(inventory_items, many=True)
            return Response(serializer.data)
        except PlayerTraits.DoesNotExist:
            return Response({'message':'Player not found'})


class InventoryAdd(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        try:
            player = PlayerTraits.objects.get(user=request.user)
            item_id = request.data.get('id')

            if item_id is not None:
                item = Item.objects.get(pk=item_id)
                inventory_item, created = Inventory.objects.get_or_create(player=player, item=item)
                if not created:
                    inventory_item.quantity +=1
                    inventory_item.save()
                return Response({'message':'Item added to inventory'})
            else:
                return Response({'message':'An error occured, item not added'})
        except PlayerTraits.DoesNotExist:
            return Response({'message':'Player not found'})
        


class InventoryRemove(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        try:
            player = PlayerTraits.objects.get(user=request.user)
            item_id = request.data.get('id')

            if item_id is not None:
                item = Item.objects.get(pk=item_id)
                inventory_item = Inventory.objects.filter(player=player, item=item)
                if inventory_item:
                    if inventory_item > 1:
                        inventory_item -=1
                        inventory_item.save()
                    else:
                        inventory_item.delete()
                    return Response({'message': 'Item removed from inventory'})
                else:
                    return Response({'message':'Item not found'})
            else:
                return Response({'message':'An error occured '})
        except PlayerTraits.DoesNotExist:
            return Response({'message':'Player not found'})