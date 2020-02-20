from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
 

# Create your models here.
class Neighborhood(models.Model):
    hoodpic=models.ImageField(upload_to='images',blank=True)
    hoodname=models.CharField(max_length=30)
    numberofpeople=models.IntegerField(blank=True,default=0)
    hoodlocation=models.CharField(max_length=30)
    
    def __str__(self):
        return self.hoodname
    
    def savehood(self):
        self.save()
    
class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to='images/',blank=True)
    editor=models.OneToOneField(User,on_delete=models.CASCADE)
    Hood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    email=models.CharField(max_length=60)
    
class Business(models.Model):
    businesspic=models.ImageField(upload_to='images/',blank=True)
    businessname=models.CharField(max_length=30)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    area=models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)
    businessemail=models.CharField(max_length=30)
    pub_date=models.DateTimeField(auto_now_add=True)
    
class News(models.Model):
    newspic=models.ImageField(upload_to='images/',blank=True)
    title=models.CharField(max_length=30)
    description=HTMLField()
    newsloaction=models.CharField(max_length=30)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)