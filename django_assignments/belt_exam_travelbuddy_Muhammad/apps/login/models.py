from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be more than 2 characters"

        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be more than 2 characters"

        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid Email"
        
        if len(postData['password']) < 8:
            errors["password"] = "Invalid Password!"
        
        if postData['password'] != postData['passwordconf'] :
            errors["passwordconf"] = "Invalid Password!"

        if len(Users.objects.filter(email = postData['email'])) > 0:
            errors['email'] = "Email is already in the database!"

        return errors

    def login_validator(self , postData):
        errors = {}
        if len(postData['password']) < 8:
            errors["password"] = "Invalid Password"

        if len(Users.objects.filter(email = postData['email'])) < 1:
            errors['email'] = "Invalid Email!"
            return errors
        current_user = Users.objects.filter(email = postData['email'])[0]
        password_check = bcrypt.checkpw(postData['password'].encode('utf8'), current_user.password.encode('utf8'))
        if password_check == False:
            errors['password'] = 'Invalid password'
        return errors

class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        if len(postData['description']) < 5:
            errors['description'] = "Description is too short"
        if len(postData['location']) < 5:
            errors['location'] = "Location name is too short"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UsersManager()

class Trips(models.Model):
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_date_from = models.DateField(max_length=255)
    travel_date_to = models.DateField(max_length=255)
    user_created = models.ForeignKey(Users, related_name="trip_created")
    planned_by = models.ManyToManyField(Users, related_name="users_booked")
    objects = TripManager()

