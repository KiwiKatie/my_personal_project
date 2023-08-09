from django.db import models

class Player(models.Model):
    # id  = models.IntegerField
    name = models.CharField(max_length=255)
    user = models.EmailField(max_length=255)
    # traits = models.OneToOneField(PlayerTraits, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class PlayerTraits(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='player_traits')
    charisma = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)

    def __str__(self):
        return f" CHA:{self.charisma}, DEX:{self.dexterity}, STR:{self.strength}, INT:{self.intelligence}"


class GameProgress(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    last_battle = models.CharField(max_length=255)
    health = models.IntegerField(default=15)
    damage =models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    story_section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.player} your health is {self.health}, and your level is {self.level}"

