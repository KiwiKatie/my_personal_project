from rest_framework.serializers import ModelSerializer
from .models import PlayerTraits, GameProgress


class PlayerTraitsSerializer(ModelSerializer):
    class Meta:
        model = PlayerTraits
        fields = ['user', 'name', 'charisma', 'dexterity', 'strength', 'intelligence']


class GameProgressSerializer(ModelSerializer):
    class Meta:
        model = GameProgress
        fields = ['player', 'last_battle', 'damage', 'health', 'level', 'story_section']