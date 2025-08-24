from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class FitnessProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="fitness_profile",
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    weight = models.FloatField(
        null=True,
        blank=True,
    )  # in kilograms
    height = models.FloatField(
        null=True,
        blank=True,
    )  # in centimeters
    goal = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
    activity_level = models.CharField(
        choices=[
            ("sedentary", "Sedentary"),
            ("lightly_active", "Lightly Active"),
            ("moderately_active", "Moderately Active"),
            ("very_active", "Very Active"),
        ],
        default="sedentary",
        max_length=20,
    )

    def __str__(self):
        return self.user.username