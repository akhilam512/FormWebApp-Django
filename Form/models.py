from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=50)
	age = models.DecimalField(decimal_places=1, max_digits=3)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	gender = models.CharField(max_length=10)
