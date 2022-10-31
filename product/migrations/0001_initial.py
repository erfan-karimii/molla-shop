# Generated by Django 4.1 on 2022-10-09 23:05

import ckeditor.fields
import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام دسته بندی')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیح دسته بندی')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('tozihat', models.CharField(max_length=300, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('alt', models.CharField(max_length=100, null=True)),
                ('image_2', models.ImageField(null=True, upload_to='')),
                ('alt_2', models.CharField(max_length=100, null=True)),
                ('price_asli', models.IntegerField(null=True, verbose_name='قیمت اصلی')),
                ('tedad_mahsol', models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='تعداد محصول')),
                ('info', ckeditor.fields.RichTextField()),
                ('more_info', ckeditor.fields.RichTextField(null=True)),
                ('takhfif', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='درصد تخفیف')),
                ('color_asli', colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=[('#FFFFFF', 'white'), ('#000000', 'black')])),
                ('size_asli', models.CharField(max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20, verbose_name='سایز')),
                ('Ekhtelaf', models.IntegerField(null=True, verbose_name='اختلاف قیمت')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
            options={
                'verbose_name': 'سایز های بیشتر کیف',
                'verbose_name_plural': 'سایز های بیشتر کیف',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='product.tags'),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس محصول')),
                ('alt', models.CharField(max_length=150, verbose_name='توضیحات عکس')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=[('#FFFFFF', 'white'), ('#000000', 'black')])),
                ('Ekhtelaf', models.IntegerField(null=True, verbose_name='اختلاف قیمت')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
            options={
                'verbose_name': 'رنگ های بیشتر',
                'verbose_name_plural': 'رنگ های بیشتر',
            },
        ),
    ]
