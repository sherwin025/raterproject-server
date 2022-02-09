from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.forms import ValidationError
from django.http import HttpResponseServerError

from raterprojectapi.models import Game
from raterprojectapi.models.player import Player

class GameView(ViewSet):
    def retrieve(self, request,pk):
        try: 
            game = Game.objects.get(pk=pk)
            serializer = GameSerizalier(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self,request):
        games = Game.objects.all()
        game_cat = request.query_params.get('category', None)
        if game_cat is not None:
            games = games.filter(game_category=game_cat)
        serializer = GameSerizalier(games, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        theplayer = Player.objects.get(user=request.auth.user)
        try: 
            serializer = CreateGameSerizalier(data=request.data)
            serializer.is_valid(raise_exception=True)
            game = serializer.save(createdby=theplayer)
            game.categories.add(request.data["categories"]) #takes category id and creates gamecategory use "set" for multiple 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        try:
            game = Game.objects.get(pk=pk)
            serializer = CreateGameSerizalier(game, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
      
    
class GameSerizalier(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("id", "title", "description", "designer", "year_released", "num_of_players", "est_time_to_play", "age_recomendation", "categories", "createdby", "average_rating")
        depth = 1
        
class CreateGameSerizalier(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("id", "title", "description", "designer", "year_released", "num_of_players", "est_time_to_play", "age_recomendation")
