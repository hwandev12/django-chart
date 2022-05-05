# from colorfield.fields import ColorField
from django.db import models
from django.shortcuts import render


class Post(models.Model):

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "My posts"

    name = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Expense(models.Model):

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "My Dashboard Expenses"

    name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "My Users"

    index = models.IntegerField()
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    owner = models.CharField(max_length=60)
    open_date = models.CharField(max_length=40)
    status = models.CharField(max_length=20)
    impact = models.FloatField()

    def __str__(self):
        return self.name


class Line(models.Model):

    class Meta:
        verbose_name = "Line"
        verbose_name_plural = "My Lines"

    date = models.CharField(max_length=40)
    value = models.IntegerField()

    def __str__(self):
        return self.date


class Time(models.Model):

    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "My Times"

    hour = models.CharField(max_length=40)
    weekday = models.CharField(max_length=30)
    value = models.IntegerField()
    # color = ColorField(default='#FF0000')

    def __str__(self):
        return self.hour

class Flow(models.Model):
    
    class Meta:
        verbose_name = "Flow"
        verbose_name_plural = "My Flow Times"
        
    value = models.IntegerField()
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
