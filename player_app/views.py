from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Player, PlayerTraits, GameProgress
from .serializers import PlayerSerializer, PlayerTraitsSerializer, GameProgressSerializer
# from rest_framework import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST


##user Auth
# class PlayerDetails(APIView):
#     # permission_classes=[IsAuthenticated]

#     def get(self, request):
#         player = Player.objects.get(user=request.user)
#         serializer = PlayerSerializer(player, many=True)
#         return Response(serializer.data)
    
class PlayerDetails(APIView):

    def get(self, request, player_id):
        try:
            player = Player.objects.get(id=player_id)
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        except Player.DoesNotExist:
            return Response({'message':'Player not found'})



# class PlayerTraits(APIView):
#     # permission_classes=[IsAuthenticated]

#     def get(self, request):
#         player = Player.objects.get(user=request.user)
#         traits = PlayerTraits.objects.get(player=player)
#         serializer = PlayerTraits(traits, many=True)
#         return Response(serializer.data)

class PlayerTraitsView(APIView):

    def get(self, request, player_id):
        try:
            # player = Player.objects.get(id=player_id)
            # print(player)
            traits = PlayerTraits.objects.get(player_id=player_id)
            # traits = PlayerTraits.objects.all()
            # all_trait = PlayerTraits.objects.all()
            # print(traits)
            serializer = PlayerTraitsSerializer(traits, many=False)
            return Response(serializer.data)
        except Player.DoesNotExist:
            return Response({'message':'Player not found'})
        



# class GameProgress(APIView):
#     # permission_classes=[IsAuthenticated]

#     def get(self, request):
#         player = Player.objects.get(user=request.user)
#         progress = GameProgress.objects.get(player=player)
#         serializer = GameProgressSerializer(progress, many=True)
#         return Response(serializer.data)

#     def patch(self, request):
#         player = Player.objects.get(user=request.user)
#         progress = GameProgress.objects.get(player=player)

#         new_health = progress.health - request.data.get('damage',0)
#         progress.health = new_health

#         new_level = progress.level + request.data.get('levels',0)
#         progress.level=new_level

#         new_section = request.data.get('new_section')
#         if new_section is not None:
#             progress.current_section_index = new_section
#             progress.save()
        
#         progress.save()
#         serializer = GameProgressSerializer(progress)
#         return Response(serializer.data)

class GameProgressView(APIView):

    def get(self, request, player_id):
        try:
            # player = Player.objects.get(id=player_id)
            progress = GameProgress.objects.get(player_id=player_id)
            serializer = GameProgressSerializer(progress)
            return Response(serializer.data)
        except Player.DoesNotExist:
            return Response({'message':'Player not found'})

    def patch(self, request, player_id):
        try:    
            player = Player.objects.get(id=player_id)
            progress = GameProgress.objects.get(player=player)

            new_health = progress.health - request.data.get('damage',0)
            progress.health = new_health

            new_level = progress.level + request.data.get('levels',0)
            progress.level=new_level

            new_section = request.data.get('new_section')
            if new_section is not None:
                progress.current_section_index = new_section
                progress.save()
            
            progress.save()
            serializer = GameProgressSerializer(progress)
            return Response(serializer.data)
        except Player.DoesNotExist:
            return Response({'message':'Player not found'})