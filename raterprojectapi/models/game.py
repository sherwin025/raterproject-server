from django.db import models
from .game_rating import GameRating


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    designer = models.CharField(max_length=100)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    est_time_to_play = models.FloatField()
    age_recomendation = models.CharField(max_length=10)
    categories = models.ManyToManyField(
        "Category", through="GameCategory", related_name="categories")
    createdby = models.ForeignKey('Player', on_delete=models.CASCADE)

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = GameRating.objects.filter(game=self)

        if (len(ratings) > 0):
            total_rating = 0
            for rating in ratings:
                total_rating += rating.rating

            length = len(ratings)

            return total_rating / length
        return 0
