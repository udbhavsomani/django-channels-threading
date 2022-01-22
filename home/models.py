import email
from unicodedata import name
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
