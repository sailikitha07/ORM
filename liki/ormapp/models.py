from django.db import models
from django.contrib import admin
class Movie(models.Model):
    user_id = models.CharField(max_length=20)
    user_email = models.CharField(max_length=200)
    movie_name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="Movie Rating (e.g., 8.5)")

class MovieAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_email', 'movie_name', 'rating')
