from pickle import TRUE
from django.db import models

WEATHER = (('C' , 'Cold') , ('H' , 'Hot') , ('M' , 'Mild'))
CLASS = (('U' , 'Upper') , ('M' , 'Middle') , ('L' , 'Lower'))

class Distrito(models.Model):
    name = models.CharField(max_length = 40, blank = False, null = False)
    weather = models.CharField(choices = WEATHER, max_length = 1, blank = True, null = True)
    s_class = models.CharField(choices = CLASS, max_length = 1, blank = True, null = True)
    extra = models.TextField(blank = True, null = True)

NATURE_TYPE = (('N' , 'Neutral') , ('C' , 'Chaotic'))

class Tributo(models.Model):
    name = models.CharField(max_length = 40, blank = False, null = False)
    ## picture = asdfsgdh
    district = models.ForeignKey(Distrito, blank = False, null = False, on_delete=models.CASCADE)
    nature = models.CharField(choices = NATURE_TYPE, max_length = 1, blank = True, null = True)
    extra = models.TextField(blank = True, null = True)

