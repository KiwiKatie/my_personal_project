from rest_framework.serializers import ModelSerializer
from .models import Player, PlayerTraits, GameProgress

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'user']


class PlayerTraitsSerializer(ModelSerializer):
    class Meta:
        model = PlayerTraits
        fields = ['id', 'charisma', 'dexterity', 'strength', 'intelligence', 'player_id']


class GameProgressSerializer(ModelSerializer):
    class Meta:
        model = GameProgress
        fields = ['id', 'last_battle', 'health', 'damage', 'level', 'story_section', 'player_id']