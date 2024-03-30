from django.db import models
from os import path
from django.conf import settings

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    race = models.CharField(max_length=20)
    hometown = models.CharField(max_length=20)
    age = models.CharField(max_length=6)
    char_type = models.CharField(max_length=20)
    img = models.ImageField(blank=True, upload_to='character')

    def __str__(self):
        return f'-- {self.name} from {self.hometown} --'

class Esper(models.Model):
    name_esper = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=60)
    sign = models.CharField(max_length=50)
    element = models.CharField(max_length=50)
    img = models.ImageField(blank=True, upload_to='esper')
    

    def __str__(self):
        return f'-- {self.name_esper} --'