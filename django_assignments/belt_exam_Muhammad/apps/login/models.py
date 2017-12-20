from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors["name"] = "First name should be more than 5 characters"
        if len(postData['last_name']) < 3:
            errors["name"] = "Last name should be more than 5 characters"  
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "This email is invalid"  
        if len(postData['password']) < 8:
            errors["password"] = "User password should be more than 10 characters"
        return errors

    def login_validator(self , postData):
        errors = {}
        if len(postData['password']) < 9:
            errors["password"] = "Password  is invalid"
        if len(Users.objects.filter(email = postData['email'])) < 1:
            errors['email'] = "Email is invalid!"
            return errors
        current_user = Users.objects.filter(email = postData['email'])[0]
        password_check = bcrypt.checkpw(postData['password'].encode(), current_user.password.encode())
        if password_check == False:
            errors['password'] = 'Password is invalid'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    birthday = models.DateField(auto_now=False)
    objects = UserManager()

class Poke(models.Model):
    pokeduser = models.ForeignKey(User, related_name = "poked_user")
    pokeruser = models.ForeignKey(User, related_name = "poker_user")
    count = models.IntegerField(default = 0, blank=False, null=True)
    countsum = models.IntegerField(default = 0, blank=False, null=True)
