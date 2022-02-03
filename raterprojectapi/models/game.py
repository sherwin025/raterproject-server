from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    designer = models.CharField(max_length=100)
    year_released = models.IntegerField()
    num_of_players =  models.IntegerField()
    est_time_to_play = models.FloatField()
    age_recomendation = models.CharField(max_length=10)
    categories = models.ManyToManyField("Category", through="GameCategory", related_name="categories")