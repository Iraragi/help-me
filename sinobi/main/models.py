from django.db import models
from django.urls import reverse





class Roll(models.Model):
    name = models.CharField(max_length=20, help_text="name of roll or sushi")
    summary = models.TextField(max_length=1000, help_text="describe roll or sushi")

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=20, help_text="name of pizza")
    summary = models.TextField(max_length=1000, help_text="describe pizza")

    def __str__(self):
        return self.name


class Burger(models.Model):
    name = models.CharField(max_length=20, help_text="name of burger")
    summary = models.TextField(max_length=1000, help_text="describe burger")

    def __str__(self):
        return self.name


class Snack(models.Model):
    name = models.CharField(max_length=20, help_text="name of snack")
    summary = models.TextField(max_length=1000, help_text="describe snack")

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=20, help_text="name of drink")

    def __str__(self):
        return self.name


class Set(models.Model):
    title = models.CharField(max_length=20)
    summary = models.TextField(max_length=1000, help_text="describe set")
    roll = models.ManyToManyField(Roll, help_text="Select a rolls for this set")

    def __str__(self):
        return self.title


