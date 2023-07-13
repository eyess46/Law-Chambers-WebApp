from django.db import models

# Create your models here.


class Feature(models.Model):
    
    name = models.CharField(max_length=100) 
    details = models.CharField(max_length=500)


class New(models.Model):

    newsdetails = models.CharField(max_length=300)
    posted_at = models.DateTimeField()


class Contactform(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(unique= True)
    subject = models.CharField(max_length= 100)
    message = models.CharField(max_length= 900)
