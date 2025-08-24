from django.contrib import admin
from .models import FitnessProfile


@admin.register(FitnessProfile)
class FitnessProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'height', 'goal', 'activity_level')
    list_filter = ('activity_level', 'gender')
    search_fields = ('user__username', 'user__email')

