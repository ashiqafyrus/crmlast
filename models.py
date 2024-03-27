from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class ImageApp(models.Model):
    name=models.CharField(max_length=225)
    price=models.IntegerField(null=True,default=0)
    
class Archive(models.Model):
    
    app=models.ForeignKey(ImageApp,on_delete=models.CASCADE,null=True)