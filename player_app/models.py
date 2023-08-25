from django.db import models
from user_app.models import Usr
from django.core.exceptions import ValidationError


class PlayerTraits(models.Model):
    user = models.OneToOneField(Usr, on_delete=models.CASCADE, related_name='users', null=True)
    name = models.CharField(max_length=255, default='The Nameless')
    charisma = models.PositiveIntegerField(default=0)
    dexterity = models.PositiveIntegerField(default=0)
    strength = models.PositiveIntegerField(default=0)
    intelligence = models.PositiveIntegerField(default=0)

    def validate_traits_total(self):
        total_traits = self.charisma + self.dexterity + self.strength + self.intelligence
        print(total_traits)
        if total_traits > 15:
            raise ValidationError("Total traits must be equal to 15.")

    def save(self, *args, **kwargs):
        self.full_clean() 
        print("Validation successful!")
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name}: CHA:{self.charisma}, DEX:{self.dexterity}, STR:{self.strength}, INT:{self.intelligence}"


class GameProgress(models.Model):
    player = models.OneToOneField(PlayerTraits, on_delete=models.CASCADE)
    last_battle = models.CharField(max_length=255)
    damage =models.IntegerField(default=0)
    health = models.IntegerField(default=15)
    level = models.IntegerField(default=1)
    story_section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.player} your health is {self.health}, and your level is {self.level}"



