from django.db import models
from player_app.models import Player

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField

    def __str__(self):
        return f"{self.name}"

class Inventory(models.Model):
    player = models.ForeignKey(Player, related_name='inventory', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    
