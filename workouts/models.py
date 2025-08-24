from django.contrib.auth import get_user_model
from django.db import models


class WorkoutType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class WorkoutSession(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="workouts",
    )
    type = models.ForeignKey(
        WorkoutType,
        on_delete=models.CASCADE,
        related_name="workout_sessions",
    )
    date = models.DateTimeField(
        auto_now_add=True,
    )
    notes = models.TextField(
        null=True,
        blank=True,
    )

    @property
    def duration(self):
        pass

    @property
    def calories_burned(self):
        pass
