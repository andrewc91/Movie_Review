from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
import re

name_regex = re.compile(r"^[a-zA-Z\s]+$")

# Create your models here.
class DirectorManager(models.Manager):
    def director_validator(self, input):
        errors = []

        if len(input['director']) == 0:
            errors.append("Please enter a director")

        if len(input['director']) < 5:
            errors.append("Director's name must have at least 5 characters")

        if not name_regex.match(input['director']):
            errors.append("Director's name must have letters only")

        if len(errors) == 0:
            Director.objects.create(name=input['director'])
            return (True, "Successfully added director")
        else:
            return (False, errors)

class Director(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DirectorManager()

class MovieManager(models.Manager):
    def movie_validator(self, input):
        errors = []

        if len(input['movie']) == 0:
            errors.append("Please enter a movie")

        if len(input['movie']) < 2:
            errors.append("Movie must have at least 2 characters")

        if len(errors) == 0:
            Movie.objects.create(title=input['movie'])
            return (True, "Successfully added movie")
        else:
            return (False, errors)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.ForeignKey(Director)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MovieManager()

class ReviewManager(models.Manager):
    def review_validator(self, input):
        errors = []

        if len(input['description']) == 0:
            errors.append("Please enter a description")

        if len(input['description']) < 5:
            errors.append("Description must be at least 5 characters. Be descriptive!")

        if not (input['rating']):
            errors.append("Please select a rating for this movie")

        if len(errors) == 0:
            Review.objects.create(description=input['description'], rating=input['rating'])
            return (True, "Successfully added review")
        else:
            return (False, errors)

class Review(models.Model):
    description = models.TextField
    rating = models.IntegerField()
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
