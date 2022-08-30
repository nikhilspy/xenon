from django.db import models
# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=150)
    

class Query(models.Model):
    userid= models.ForeignKey(User,on_delete=models.CASCADE)
    Contact = models.CharField(max_length=50)
    Message = models.TextField(max_length=500)