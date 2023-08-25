from django.db import models
from player_app.models import PlayerTraits


    
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(null=True)

    def __str__(self):
        return f"{self.name}"


class Inventory(models.Model):
    player = models.ForeignKey(PlayerTraits, related_name='inventory', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0) 