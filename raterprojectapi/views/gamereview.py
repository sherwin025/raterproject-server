from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.forms import ValidationError
from django.http import HttpResponseServerError

from raterprojectapi.models import GameReviews
from raterprojectapi.models.player import Player

class ReviewView(ViewSet):
    def list(self, request):
        reviews = GameReviews.objects.all()
        game_reviews = request.query_params.get("game", None)
        if game_reviews is not None:
            reviews = reviews.filter(game_id=game_reviews)
        serializer = ReviewSerizalier(reviews, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        theplayer = Player.objects.get(user=request.auth.user)
        try:
            serializer = CreateReviewSerizalier(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(player=theplayer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class ReviewSerizalier(serializers.ModelSerializer):
    class Meta:
        model = GameReviews
        fields = ("id","player", "game", "review")
        
        
class CreateReviewSerizalier(serializers.ModelSerializer):
    class Meta:
        model = GameReviews
        fields = ("game", "review")
        