from django.core.validators import MinLengthValidator
from django.db import models
from fruitipediaApp.profiles.validators import name_starts_with_letter


class Profile(models.Model):
    first_name = models.CharField(max_length=25, validators=(MinLengthValidator(2), name_starts_with_letter),)
    last_name = models.CharField(max_length=35, validators=(MinLengthValidator(1), name_starts_with_letter),)
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=20, validators=(MinLengthValidator(8),),
                                help_text='*Password length requirements: 8 to 20 characters')
    image = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, default=18)
