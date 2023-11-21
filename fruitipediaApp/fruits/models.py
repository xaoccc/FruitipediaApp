from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaApp.fruits.validators import name_consists_with_letter_only_validator


# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=40,
        unique=True,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            MinLengthValidator(2),
            name_consists_with_letter_only_validator,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=False,
        blank=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
