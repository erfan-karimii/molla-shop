# Generated by Django 4.0.4 on 2022-10-27 07:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_show',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.PositiveIntegerField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
