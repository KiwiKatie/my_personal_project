from django.db import models

class Monster(models.Model):
    name = models.CharField(max_length=255)
    health = models.IntegerField(default=5)
    

    def __str__(self):
        return self.name

