from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import  PlayerTraits, GameProgress
from .serializers import  PlayerTraitsSerializer, GameProgressSerializer
from django.contrib.auth import get_user
import json
from django.http import JsonResponse

class PlayerTraitsView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        try:
            traits = PlayerTraits.objects.get(user=request.user)
            serializer = PlayerTraitsSerializer(traits, many=False)
            return Response(serializer.data)
        except PlayerTraits.DoesNotExist:
            return Response({'message':'Player not found'})
        
        
class CreatePlayerView(APIView):
    permission_classes = [IsAuthenticated]
        
    def post(self, request):
        serializer = PlayerTraitsSerializer(data=request.data)
        print(serializer)
        print(request.user.id)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    

class StoryAndChoices(APIView):

    def get(self, request):
        with open('./story.json', 'r') as json_file:
            story_data = json.load(json_file)
        return JsonResponse(story_data)
        


class GameProgressView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        try:     
            player_traits = PlayerTraits.objects.get(user=request.user)
            progress, _ = GameProgress.objects.get_or_create(player=player_traits)
            print(progress)
            serializer = GameProgressSerializer(progress)
            return Response(serializer.data)
        except PlayerTraits.DoesNotExist:
            return Response({'message': 'Player not found'})

    def put(self, request):
        try:
            print(request.body)
            player_traits = PlayerTraits.objects.get(user=request.user)
            progress, created = GameProgress.objects.get_or_create(player=player_traits)


            damage = request.data.get('damage', 0)
            health = request.data.get('health', progress.health) 

            if damage == 0:
                new_health = health
            elif damage > 0:
                new_health = progress.health - abs(damage)
            else:
                new_health = progress.health
            progress.health = new_health

            level = request.data.get('level', progress.level)
            progress.level = level 

            new_section = request.data.get('story_section')
            if new_section is not None:
                progress.story_section = new_section
            progress.save()

            serializer = GameProgressSerializer(progress)
            return Response(serializer.data)
        except PlayerTraits.DoesNotExist:
            return Response({'message': 'Player not foundsssss'})
        
    
    def post(self, request):
        serializer = GameProgressSerializer(data=request.data)
        print(serializer)
        print(request.user.id)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)




