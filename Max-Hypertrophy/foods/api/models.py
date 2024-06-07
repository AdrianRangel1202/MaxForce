from djongo import models


class Foods(models.Model):
    name = models.CharField(max_length= 200)
    proteins = models.IntegerField()
    carbohydrates = models.IntegerField()
    fats = models.IntegerField()
    calories = models.IntegerField()

