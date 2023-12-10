from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class popular(models.Model):
    blog_img = models.FileField(upload_to="blog-img/",max_length=250,null=None)
    blog_title = models.CharField(max_length=100)
    blog_desc = HTMLField()

    blog_title2 = models.CharField(max_length=100)
    blog_desc1 = HTMLField()


class latest(models.Model):
    blog_img = models.FileField(upload_to="blog-img/",max_length=250,null=None)
    blog_title = models.CharField(max_length=100)

    blog_title2 = models.CharField(max_length=100)
    blog_desc = HTMLField()
    

class trending(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_img = models.FileField(upload_to="blog-img/",max_length=250,null=None)
    
    blog_title2 = models.CharField(max_length=100)
    blog_desc = HTMLField()





class aboutus(models.Model):
    blog_img1 = models.FileField(upload_to="blog-img/",max_length=250,null=None)
    blog_img2 = models.FileField(upload_to="blog-img/",max_length=250,null=None)
    blog_title2 = models.CharField(max_length=100)
    blog_title1 = models.CharField(max_length=100)
    blog_desc1 = HTMLField()
    blog_desc2 = HTMLField()
    blog_desc3 = HTMLField()
  

class allblogs(models.Model):
    blog_img = models.FileField(upload_to="blog-img/",max_length=250,null=None)
    blog_title = models.CharField(max_length=100)
    
   


