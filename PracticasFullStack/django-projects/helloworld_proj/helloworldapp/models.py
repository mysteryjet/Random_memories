from django.db import models

# Create your models here.
class FirstModel(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    isActive = models.BooleanField()
    result = models.TextField()

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    id = models.CharField(max_length=100, primary_key=100)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True, auto_now_add=False)
    size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Class(models.Model):

    id = models.CharField(max_length=100, primary_key=100)
    class_name = models.CharField(max_length=254, unique=True)
    floor = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'class'
        verbose_name_plural = 'classes'
