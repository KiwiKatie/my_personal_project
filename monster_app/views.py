from django.shortcuts import render
from random import randint
from rest_framework.response import Response
from rest_framework.views import APIView
from monster_app.models import Monster
from player_app.models import PlayerTraits
from player_app.models import GameProgress
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
import requests
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT,HTTP_200_OK

class CombatView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request, custom_monster_name):
        print(request)
        endpoint = f"https://www.dnd5eapi.co/api/monsters/{custom_monster_name}"
        response = requests.get(endpoint)
        monster_data = response.json()
        return Response(monster_data, status=HTTP_200_OK)

    
    def put(self, request, custom_monster_name):
        print(request.body)
        try:
            player = PlayerTraits.objects.get(user=request.user)
            player_choice = request.data.get('player_choice')
            monster_health = request.data.get('monster_health')
            # endpoint = f"https://www.dnd5eapi.co/api/monsters/{custom_monster_name}"

            # response = requests.get(endpoint)
            # monster = response.json()  
            #print(monster)
            
            # monster_data.hit_points
            player_attack, monster_attack = self.calculate_combat_outcome(player, monster_health)
            progress = GameProgress.objects.get(player=player)

            progress.health-= monster_attack
            monster_health -= player_attack
            progress.save()
            
     
            battle_outcome = self.handle_battle_outcome( player_attack, monster_attack, progress.health, monster_health)  

            return Response(battle_outcome, status=HTTP_200_OK)
        except (PlayerTraits.DoesNotExist, Monster.DoesNotExist):
            return Response({'message': 'Player or monster not found'})
        
    def calculate_combat_outcome(self, player, monster_health):

            # Calculate the player's attack based on their chosen attack_choice
            player_choice = self.request.data.get('player_choice')
            player_choice = self.request.data.get('player_choice')
            if player_choice == 'attack1' or player_choice == 'attack2':
                player_attack = randint(1, player.strength)
            else:
                player_attack = 0 

            # Calculate a random monster attack value between 1 and the monster's hit points
            monster_attack = randint(1, monster_health)
            return player_attack, monster_attack
            
    
    
    def handle_battle_outcome(self, player_attack, monster_attack, health, monster_health):
        if health<= 0:
            return {
                'message': 'You were defeated!',
                'player_health': 0,
                'player_attack': 0,
                'monster_health': monster_health,
                'monster_attack': 0
            }
        elif monster_health <= 0:
            return {
                'message': 'You defeated the monster!',
                'player_health': health,
                'player_attack': 0,
                'monster_health': 0,
                'monster_attack': 0
            }
        else:
            return {
                'message': 'Battle continues...',
                'player_health': health,
                'player_attack': player_attack,  
                'monster_health': monster_health,
                'monster_attack': monster_attack  
            }
#  def post(self, request, custom_monster_name):
#         endpoint = f"https://www.dnd5eapi.co/api/monsters/{custom_monster_name}"
#         response = requests.get(endpoint)
#         monster_data = response.json()
#         data = {"name": monster_data["index"], "health": monster_data["hit_points"]}
#         monster = Monster.objects.create(**data)
#         monster.save()
#         return Response(data, status=HTTP_201_CREATED)

#     def get(self, request, custom_monster_name):
#         monster = Monster.objects.get(name=custom_monster_name)
#         data = {"name": monster.name, "health": monster.health}
#         return Response(data, status=HTTP_200_OK)

    
#     def put(self, request, custom_monster_name):
#         print(request.body)
#         try:
#             player = PlayerTraits.objects.get(user=request.user)
#             player_choice = request.data.get('player_choice') 
#             monster = Monster.objects.get(name=custom_monster_name)
            
#             player_attack, monster_attack = self.calculate_combat_outcome(player, monster, monster.health)
#             progress = GameProgress.objects.get(player=player)

#             progress.health-= monster_attack
#             monster.health -= player_attack
#             progress.save()
#             monster.save()
     
#             battle_outcome = self.handle_battle_outcome( player_attack, monster_attack, progress.health, monster.health)  
#             return Response(battle_outcome, status=HTTP_200_OK)
#         except (PlayerTraits.DoesNotExist, Monster.DoesNotExist):
#             return Response({'message': 'Player or monster not found'})
        
#     def calculate_combat_outcome(self, player, monster, monster_health):

#             # Calculate the player's attack based on their chosen attack_choice
#             player_choice = self.request.data.get('player_choice')
#             player_choice = self.request.data.get('player_choice')
#             if player_choice == 'attack1' or player_choice == 'attack2':
#                 player_attack = randint(1, player.strength)
#             else:
#                 player_attack = 0 

#             # Calculate a random monster attack value between 1 and the monster's hit points
#             monster_attack = randint(1, monster_health)
#             return player_attack, monster_attack
            
    
    
#     def handle_battle_outcome(self, player_attack, monster_attack, health, monster_health):
#         if health<= 0:
#             return {
#                 'message': 'You were defeated!',
#                 'player_health': 0,
#                 'player_attack': 0,
#                 'monster_health': monster_health,
#                 'monster_attack': 0
#             }
#         elif monster_health <= 0:
#             return {
#                 'message': 'You defeated the monster!',
#                 'player_health': health,
#                 'player_attack': 0,
#                 'monster_health': 0,
#                 'monster_attack': 0
#             }
#         else:
#             return {
#                 'message': 'Battle continues...',
#                 'player_health': health,
#                 'player_attack': player_attack,  
#                 'monster_health': monster_health,
#                 'monster_attack': monster_attack  
#             }
