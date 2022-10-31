from turtle import title
from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام مشتری')
    email = models.EmailField(verbose_name='ایمیل مشتزی',null=True)
    phone = models.IntegerField()
    title = models.CharField(max_length=300)
    body = models.TextField()
    
    def __str__(self):
        return self.name

class KhabarName(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email

class OurShop(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام فروشکاه')
    image = models.ImageField(verbose_name='عکس فروشگاه')
    alt = models.CharField(max_length = 200,null=True)
    address = models.TextField(verbose_name='ادرس فروشگاه')
    work_time = models.CharField(max_length=200,verbose_name='تایم کاری')
    work_days = models.CharField(max_length=200,verbose_name='روزهای کاری')
    
    def __str__(self):
        return self.name
    
class ContactDetail(models.Model):
    telephone = models.CharField(max_length=20,verbose_name='تلفن')
    email = models.CharField(max_length=254,verbose_name='ایمیل')
    image = models.ImageField(verbose_name='عکس تماس باما')
    alt = models.CharField(max_length = 200,null=True)
    address = models.CharField(max_length=300,verbose_name='ادرس فروشگاه')
    work_days = models.CharField(max_length=200,verbose_name='روزهای کاری')
    work_time = models.CharField(max_length=200,verbose_name='تایم کاری')

    