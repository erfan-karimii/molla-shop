# Generated by Django 4.1 on 2022-10-09 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=20, verbose_name='تلفن')),
                ('email', models.CharField(max_length=254, verbose_name='ایمیل')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس تماس باما')),
                ('alt', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=300, verbose_name='ادرس فروشگاه')),
                ('work_days', models.CharField(max_length=200, verbose_name='روزهای کاری')),
                ('work_time', models.CharField(max_length=200, verbose_name='تایم کاری')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام مشتری')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='ایمیل مشتزی')),
                ('phone', models.IntegerField()),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='KhabarName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OurShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام فروشکاه')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس فروشگاه')),
                ('alt', models.CharField(max_length=200, null=True)),
                ('address', models.TextField(verbose_name='ادرس فروشگاه')),
                ('work_time', models.CharField(max_length=200, verbose_name='تایم کاری')),
                ('work_days', models.CharField(max_length=200, verbose_name='روزهای کاری')),
            ],
        ),
    ]
