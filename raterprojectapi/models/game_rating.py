from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class GameRating(models.Model):
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    