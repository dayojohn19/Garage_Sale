from django.core.files.storage import FileSystemStorage
from django.db import models
from django.core.files import storage

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='formImages')

    def __str__(self):
        return self.title


fs = FileSystemStorage(location='/formImages')
class Listing(models.Model):
    owner = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=64)
    link = models.ImageField(storage=fs,max_length=64,default=None,blank=True,null=True)
    time = models.CharField(max_length=64)

class Alllisting(models.Model):
    listingid = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    link = models.CharField(max_length=64,default=None,blank=True,null=True)
