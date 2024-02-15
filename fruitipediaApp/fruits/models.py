from django.core.validators import MinLengthValidator
from django.db import models
from fruitipediaApp.profiles.models import Profile
from fruitipediaApp.fruits.validators import name_consists_with_letter_only_validator


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            name_consists_with_letter_only_validator,
        ),
        unique=True,
        error_messages={'unique': "This fruit name is already in use! Try a new one."}
    )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(null=True, blank=True,)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False)


