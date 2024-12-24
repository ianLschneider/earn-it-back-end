from django.db import models

class Earner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    points = models.IntegerField()
    createdOnDate = models.DateTimeField(auto_now_add=True)
    modifiedOnDate = models.DateTimeField(auto_now=True)


class Task(models.Model):
    earner = models.ForeignKey(to=Earner, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    iconType = models.CharField(max_length=20)
    points = models.IntegerField()
    completed = models.BooleanField(default=False)
    completeByDate = models.DateField(blank=True)
    createdOnDate = models.DateTimeField(auto_now_add=True)
    modifiedOnDate = models.DateTimeField(auto_now=True)


class Reward(models.Model):
    # earner = models.ManyToManyField(Earner)
    name = models.CharField(max_length=200)
    iconType = models.CharField(max_length=20)
    points = models.IntegerField()
    createdOnDate = models.DateTimeField(auto_now_add=True)
    modifiedOnDate = models.DateTimeField(auto_now=True)