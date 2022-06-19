from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:

         verbose_name="Post"
         verbose_name_plural="Post"
    Title=models.CharField(max_length=200)
    Text=models.TextField(max_length=200)
    Author=models.TextField(max_length=200)
    Create_date=models.DateTimeField(max_length=200)
    Publisher_date=models.DateTimeField(max_length=200)

