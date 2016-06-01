from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=90)
    tag_1 = models.CharField(max_length=90)
    tag_2 = models.CharField(max_length=90)
    tag_3 = models.CharField(max_length=90)
    description = models.TextField()
