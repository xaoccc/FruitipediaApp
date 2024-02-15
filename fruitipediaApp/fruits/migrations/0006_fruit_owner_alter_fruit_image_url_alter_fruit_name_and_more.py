# Generated by Django 4.2.9 on 2024-02-15 13:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import fruitipediaApp.fruits.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('fruits', '0005_remove_fruit_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='owner',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fruit',
            name='image_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='name',
            field=models.CharField(error_messages={'unique': 'This fruit name is already in use! Try a new one.'}, max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), fruitipediaApp.fruits.validators.name_consists_with_letter_only_validator]),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='nutrition',
            field=models.TextField(blank=True, null=True),
        ),
    ]
