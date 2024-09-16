# Generated by Django 4.2.16 on 2024-09-15 15:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_productmodel_brief_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='discount_percent',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0)]),
        ),
    ]
