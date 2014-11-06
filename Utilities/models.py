from django.db import models

class Func(models.Model):
    name = models.CharField(max_length=60)
    href = models.CharField(max_length=1024)
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    funcs = models.ManyToManyField(Func)

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    registTime = models.DateField()
    email = models.EmailField()
    
class UserSetting(models.Model):
    user_id = models.ForeignKey(User)
    key = models.CharField(max_length=30)
    value = models.TextField()