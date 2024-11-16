# voting/models.py

from django.db import models
from django.contrib.auth.models import User

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)   
    email = models.EmailField()                     

class Position(models.Model):
    name = models.CharField(max_length=100)
    max_voters = models.IntegerField()
    priority = models.IntegerField()

class Candidate(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profiles/')

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
