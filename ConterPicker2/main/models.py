from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Heroe(models.Model):
    name = models.CharField('Имя героя', max_length=50)
    strength = models.CharField(max_length=5)
    agility = models.CharField(max_length=5)
    intellect = models.CharField(max_length=5)
    strengthplus = models.CharField(max_length=5)
    agilityplus = models.CharField(max_length=5)
    intellectplus = models.CharField(max_length=5)
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.name



class Conter(models.Model):
    heroe = models.OneToOneField(Heroe, on_delete = models.CASCADE, primary_key = True)
    good1 = models.ImageField(upload_to="photos/")
    good2 = models.ImageField(upload_to="photos/")
    good3 = models.ImageField(upload_to="photos/")
    bad1 = models.ImageField(upload_to="photos/")
    bad2 = models.ImageField(upload_to="photos/")
    bad3 = models.ImageField(upload_to="photos/")

    def __str__(self):
        return str(self.heroe) if self.heroe else ''


class Sborki(models.Model):
    heroe = models.ForeignKey(Heroe, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField('Описание сборки')

    def __str__(self):
        return str(self.heroe) if self.heroe else ''
