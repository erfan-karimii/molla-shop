from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class TagNav(models.Model):
    name = models.CharField(max_length=100,verbose_name='تگ ها')    
    def __str__(self):
        return self.name

class TagNewPage(models.Model):
    name = models.CharField(max_length=100,verbose_name='تگ ها')    
    def __str__(self):
        return self.name

class TagFooter(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    def __str__(self):
        return self.name

class SiteSetting(models.Model):
    name = models.CharField(max_length=50,verbose_name='اسم صاحب سایت')
    logo = models.FileField(null=True,verbose_name='لوگو')
    alt = models.CharField(max_length=100,null=True,verbose_name='توضیحات لوگو')
    favicon = models.FileField(null=True,verbose_name='آیکون')
    alt2 = models.CharField(max_length=100,null=True,verbose_name='توضیحات icon')
    text = models.CharField(max_length=500,null=True,verbose_name='متن')
    text_products_view = models.CharField(max_length=100,null=True,verbose_name='متن بالای تبلیغ')
    telephon = models.CharField(max_length=30,null=True,verbose_name='تلفن')
    link_products_view = models.CharField(max_length=100,null=True,verbose_name='لینک بالای تبلیغ')
    footer_text = models.CharField(max_length=300,null=True)
    email= models.EmailField(max_length=100,null=True,verbose_name='ایمیل')
    address = models.CharField(max_length=200,null=True,verbose_name='ادرس')
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False,verbose_name='نمایش داده شود؟')

    def __str__(self):
        return self.name

class NavOne(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100,null=True)    
    def __str__(self):
        return self.name

class NavTwo(models.Model):
    parent = models.ForeignKey(NavOne,on_delete=models.PROTECT,blank=True,null=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100,null=True)    
    def __str__(self):
        return self.name

class NavThree(models.Model):
    parent = models.ForeignKey(NavTwo,on_delete=models.PROTECT,blank=True,null=True)
    name = models.CharField(max_length=50,verbose_name='نام')
    link = models.CharField(max_length=100,blank=True,null=True,verbose_name='ادرس صفحه')

    def __str__(self):
        return self.name

class Slider(models.Model):
    text1 = models.CharField(max_length=300,null=True,verbose_name='متن ساده')
    text2= models.CharField(max_length=300,null=True,verbose_name='متن بولد')
    text3= models.CharField(max_length=300,null=True,verbose_name='متن قیمت')
    image = models.ImageField(verbose_name='عکس سلایدر')
    alt = models.CharField(max_length=100,verbose_name='توضیح عکس')
    name_button = models.CharField(max_length=100,null=True,verbose_name='متن دکمه')
    link = models.CharField(max_length=100,null=True,verbose_name='ادرس دکمه')
    def __str__(self):
        return self.name_button + " | " + self.link

class ZirSlider(models.Model):
    image1 = models.ImageField()
    text1 = models.CharField(max_length=100)
    name_button1 = models.CharField(max_length=100,null=True,verbose_name='متن دکمه')
    link1 = models.CharField(max_length=100,null=True,verbose_name='ادرس صفحه')
    
    image2 = models.ImageField()
    text2 = models.CharField(max_length=100)
    name_button2 = models.CharField(max_length=100,null=True,verbose_name='متن دکمه')
    link2 = models.CharField(max_length=100,null=True,verbose_name='ادرس صفحه')
    
    image3 = models.ImageField()
    text3 = models.CharField(max_length=100)
    name_button3 = models.CharField(max_length=100,null=True,verbose_name='متن دکمه')
    link3 = models.CharField(max_length=100,null=True,verbose_name='ادرس صفحه')
    
    image4 = models.ImageField()
    text4 = models.CharField(max_length=100)
    name_button4 = models.CharField(max_length=100,null=True,verbose_name='متن دکمه')
    link4 = models.CharField(max_length=100,null=True,verbose_name='ادرس صفحه')
    
class Tabligh(models.Model):
    image = models.ImageField()
    name_button = models.CharField(max_length=100,null=True,verbose_name='متن دکمه')
    link = models.CharField(max_length=400,null=True)
    def __str__(self):
        return self.name_button + " " + self.link

class FooterAsli(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class FooterZir(models.Model):
    footer = models.ForeignKey(FooterAsli,on_delete=models.PROTECT)
    name = models.CharField(max_length=50,verbose_name='نام')
    link = models.CharField(max_length=100,null=True,verbose_name='لینک صفحه')
    body = RichTextUploadingField(null=True,blank=True,verbose_name='بدنه')
    url_title = models.CharField(null=True,blank=True,max_length=300,verbose_name='نام صفحه')
    text = models.TextField(null=True,blank=True,verbose_name='متن')
    tag = models.ManyToManyField(TagFooter,verbose_name='تگ های فوتر')
    def __str__(self):
        return  str(self.footer.name) + " | " +  self.name + " | " + self.link
