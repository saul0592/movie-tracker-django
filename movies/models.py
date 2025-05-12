from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.year})"




# Create your models here.
