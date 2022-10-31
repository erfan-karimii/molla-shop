from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class First(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()
    image_emza = models.ImageField()
    image = models.ImageField()


class Three(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Team(models.Model):
    name =models.CharField(max_length=100,verbose_name='نام کارمند')
    image = models.ImageField()
    semat = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    link = models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return self.name