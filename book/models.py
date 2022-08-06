from enum import unique
from pyexpat import model
from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=100,null=True);
    birthday = models.DateField(null=True);
    


    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100,null=True)
    time = models.CharField(max_length=100 , null=True)
    ticket = models.CharField(max_length=100 , null=True)
    watcher = models.ForeignKey(Subscriber,on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.name

    

  
    

