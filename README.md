# Ex02 Django ORM Web Application
## Date: 21.4.2025

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## ER Diagram 

![output](<Screenshot 2025-04-21 171046.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py


from django.contrib import admin
from.models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)

models.py

from django.db import models
from django.contrib import admin
class Movie(models.Model):
    user_id = models.CharField(max_length=20)
    user_email = models.CharField(max_length=200)
    movie_name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="Movie Rating (e.g., 8.5)")

class MovieAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_email', 'movie_name', 'rating')

```

## OUTPUT

 ![output](<Screenshot 2025-04-21 182844.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
