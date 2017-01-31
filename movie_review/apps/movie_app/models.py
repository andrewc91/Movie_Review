from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
from datetime import datetime
import re

name_regex = re.compile(r"^[a-zA-Z\s]+$")

# Create your models here.
class DirectorManager(models.Manager):
    def director_validator(self, input):
        errors = []

        if len(input['new_director']) == 0:
            errors.append("Please enter a director")

        elif len(input['new_director']) < 5:
            errors.append("Director's name must have at least 5 characters")

        if not name_regex.match(input['new_director']):
            errors.append("Director's name must have letters only")

        if len(errors) == 0:
            # Director.objects.create(name=input['new_director'])
            return (True, ["Director input valid. Please fix other errors"])
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

        elif len(input['movie']) < 2:
            errors.append("Movie must have at least 2 characters")

        if len(errors) == 0:
            # Movie.objects.create(title=input['movie'], director=director)
            return (True, ["Movie input valid. Please fix other errors"])
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

        elif len(input['description']) < 5:
            errors.append("Description must be at least 5 characters. Be descriptive!")

        if not (input['rating']):
            errors.append("Please select a rating for this movie")

        if len(errors) == 0:
            # Review.objects.create(description=input['description'], rating=input['rating'])
            return (True, ["Review input valid. Please fix other errors"])
        else:
            return (False, errors)

class Review(models.Model):
    description = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

class OutingManager(models.Manager):
    def outing_validator(self, input, user):
        errors = []

        if len(input['movie_out']) == 0 or len(input['location_out']) == 0 or len(input['theater_out']) == 0 or len(input['date_out']) == 0:
            errors.append("Please fill out all fields")

        if len(input['date_out']) > 0:
            start_date = datetime.strptime(input['date_out'], "%Y-%m-%d")

            if datetime.today() >= start_date:
                errors.append('Start date must be in the future')

        if len(errors) == 0:
            outing = Outing.objects.create(movie=input['movie_out'], location=input['location_out'], theater=input['theater_out'], date=start_date, user=user)
            outing.group.add(user)
            return (True, ["Successfully added movie outing to your schedule"])

        else:
            return (False, errors)

    def join_outing(self, id, user):
        outing = Outing.objects.get(id=id)
        outing.group.add(user)
        return (True, "Successfully added trip into your schedule")

class Outing(models.Model):
    movie = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    theater = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    group = models.ManyToManyField(User, related_name="movie")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OutingManager()

class CommentManager(models.Manager):
    def comment_validator(self, input):
        errors = []

        if len(input['comment']) == 0:
            errors.append("Please do not leave comment field blank")

        if len(errors) == 0:
            pass


class Comment(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    outing = models.ForeignKey(Outing)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
