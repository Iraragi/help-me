from django.db import models
from django.urls import reverse


class Roll(models.Model):
    name = models.CharField(max_length=20, help_text="name of roll or sushi", )
    summary = models.TextField(max_length=1000, help_text="describe roll or sushi", default="default title")

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=20, help_text="name of pizza")
    summary = models.TextField(max_length=1000, help_text="describe pizza", default="default title")

    def __str__(self):
        return self.name


class Burger(models.Model):
    name = models.CharField(max_length=20, help_text="name of burger")
    summary = models.TextField(max_length=1000, help_text="describe burger", default="default title")

    def __str__(self):
        return self.name


class Snack(models.Model):
    name = models.CharField(max_length=20, help_text="name of snack")
    summary = models.TextField(max_length=1000, help_text="describe snack", default="default title")

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=20, help_text="name of drink")

    def __str__(self):
        return self.name


class Set(models.Model):
    title = models.CharField(max_length=20)
    summary = models.TextField(max_length=1000, help_text="describe set", default="default title")
    roll = models.ManyToManyField("Roll", blank=True, help_text="Select a rolls for this set")
    pizza = models.ManyToManyField("Pizza", blank=True, help_text="Select a pizza for this set")
    burger = models.ManyToManyField("Burger", blank=True, help_text="Select a burger for this set")
    snack = models.ManyToManyField("Snack", blank=True, help_text="Select a rolls snack this set")
    drink = models.ManyToManyField("Drink", blank=True, help_text="Select a drink for this set")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('set-detail', args=[str(self.id)])


