from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from fruitipediaApp.profiles.validators import name_starts_with_letter


class Profile(models.Model):
    first_name = models.CharField(validators=(MaxLengthValidator(25), MinLengthValidator(2), name_starts_with_letter),)
    last_name = models.CharField(validators=(MaxLengthValidator(35), MinLengthValidator(1), name_starts_with_letter),)
    email = models.EmailField(unique=True, validators=(MaxLengthValidator(40),))
    password = models.CharField(validators=(MaxLengthValidator(20), MinLengthValidator(8),),
                                help_text='*Password length requirements: 8 to 20 characters')
    image = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, default=18)
