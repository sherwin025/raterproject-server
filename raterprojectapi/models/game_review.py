from django.db import models

class GameReviews(models.Model):
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    review = models.CharField(max_length=500)