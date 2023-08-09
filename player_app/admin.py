from django.contrib import admin
from .models import Player, PlayerTraits, GameProgress

admin.site.register([Player, PlayerTraits, GameProgress])

