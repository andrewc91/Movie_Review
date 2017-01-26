from __future__ import unicode_literals

from django.db import models
import bcrypt, re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r"^[a-zA-Z\s]+$")

# Create your models here.

class UserManager(models.Manager):
    def register(self, input):
        errors = []

        if len(input['first_name']) < 3:
            errors.append("First name must have at least 3 characters")

        if len(input['last_name']) < 3:
            errors.append("Last name must have at least 3 characters")

        if not name_regex.match(input['first_name']):
            errors.append("First name must contain letters only")

        if not name_regex.match(input['last_name']):
            errors.append("Last name must contain letters only")

        if not email_regex.match(input['email']):
            errors.append("Not a valid email")

        if len(input['email']) < 3:
            errors.append("Email must have at least 3 characters")

        if len(input['password']) < 8:
            errors.append("Password must have at least 8 characters")

        same = User.objects.filter(email=input['email'])
        if same:
            errors.append("Email already exists!")

        if input['confirm'] != input['password']:
            errors.append("Passwords do not match!")

        if len(errors) == 0:
            pwHash = bcrypt.hashpw(input['password'].encode(), bcrypt.gensalt().encode())
            user = User.objects.create(first_name=input['first_name'], last_name=input['last_name'], email=input['email'], password=pwHash)
            return (True, user)
        else:
            return (False, errors)


    def login(self, input):
        errors = []

        if len(input['email']) == 0:
            errors.append("Please enter email")

        if len(input['password']) == 0:
            errors.append("Please enter password")

        user = User.objects.filter(email=input['email'])
        if user.exists():
            inputPw = input['password'].encode()
            hashPw = user[0].password.encode()

            if bcrypt.checkpw(inputPw, hashPw):
                return (True, user[0])
            else:
                errors.append("Incorrect password. Try again")
                return (False, errors)
        else:
            errors.append("No email and password match")
            return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
