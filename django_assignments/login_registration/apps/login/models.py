from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors["name"] = "First name should be more than 5 characters"
        if len(postData['last_name']) < 3:
            errors["name"] = "Last name should be more than 5 characters"    
        if len(postData['password']) < 8:
            errors["password"] = "User password should be more than 10 characters"
        return errors;

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    objects = UserManager()