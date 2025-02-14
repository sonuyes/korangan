from django.db import models

# Create your models here.
class reg(models.Model):
    email=models.CharField(max_length=254,blank=True, null=True) 
    image=models.ImageField(upload_to='image',blank=True, null=True)