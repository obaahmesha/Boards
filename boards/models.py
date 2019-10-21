from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#building a model for board app to have Board,Topic,Post fields

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):  #this function is use to return the string represntaion of an object
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=225)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name ='topics', on_delete=models.CASCADE)#relates to the Board class
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)#relates to the User class


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)




