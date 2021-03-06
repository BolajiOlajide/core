from django.contrib import admin

from .models import Review
from app.timetables.admin import TimeStampAdmin


@admin.register(Review)
class ReviewAdmin(TimeStampAdmin):
    """Admin customisation for Review model."""

    fields = ('user', 'anonymity_id', 'serving', 'value', 'comment',
              'date_created', 'date_modified')
