from tkinter import image_names
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings


# Create your models here.
User = settings.AUTH_USER_MODEL

class Blogpost(models.Model):
    user = models.ForeignKey(User,default = 1,null = True, on_delete = models.SET_NULL)
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    post_text = models.CharField(max_length=200)
    image_names = models.FileField(upload_to='images/', null=True)
    pub_date = models.DateField()
    
    def __str__(self):
        return self.title

class Blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    content = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return "Message from" + self.name +'-'+self.email
    
    
