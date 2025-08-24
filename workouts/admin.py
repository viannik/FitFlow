from django.contrib import admin
from .models import WorkoutType, WorkoutSession


@admin.register(WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'date', 'duration')
    list_filter = ('type', 'date')
    search_fields = ('user__username', 'type__name')
    readonly_fields = ('date', 'duration')
