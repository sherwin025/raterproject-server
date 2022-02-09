from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.forms import ValidationError
from django.http import HttpResponseServerError

from raterprojectapi.models.game_rating import GameRating
from raterprojectapi.models.player import Player

class RatingView(ViewSet):
    def retrieve(self,request, pk):
        try:
            rating = GameRating.objects.get(pk=pk)
            serializer = RatingSerizalier(rating)
            return Response(serializer.data)
        except GameRating.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
            
    def list(self, request):
        ratings = GameRating.objects.all()
        thegame = request.query_params.get('game', None)
        if thegame is not None:
            ratings = ratings.filter(game=thegame)
        serializer = RatingSerizalier(ratings, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        theplayer = Player.objects.get(user=request.auth.user)
        try:
            serializer = CreateRatingSerizalier(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(player=theplayer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk):
        try: 
            rating = GameRating.objects.get(pk=pk)
            serializer = RatingSerizalier(rating, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        rating = GameRating.objects.get(pk=pk)
        rating.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        
class RatingSerizalier(serializers.ModelSerializer):
    class Meta:
        model = GameRating
        fields = ("id", "player", "game", "rating")
        
class CreateRatingSerizalier(serializers.ModelSerializer):
    class Meta:
        model = GameRating
        fields = ("game", "rating")
        