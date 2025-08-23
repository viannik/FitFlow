from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    def __str__(self):
        return f"{self.username} {self.get_full_name()}"


class FitnessProfile(models.Model):
    user = models.OneToOneField(
        UserProfile,
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
    goals = models.CharField(
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
        return f"Fitness Profile of {self.user}"