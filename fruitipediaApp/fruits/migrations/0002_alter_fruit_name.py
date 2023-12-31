# Generated by Django 4.2.6 on 2023-11-21 11:51

import django.core.validators
from django.db import migrations, models
import fruitipediaApp.fruits.validators


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='name',
            field=models.CharField(max_length=60, validators=[django.core.validators.MinLengthValidator(2), fruitipediaApp.fruits.validators.name_consists_with_letter_only_validator]),
        ),
    ]
