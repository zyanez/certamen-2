from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "important", "short_id")
    list_filter = ("important", "created_at")
    search_fields = ("content",)
    readonly_fields = ("created_at", "id")
    date_hierarchy = "created_at"
    
    def short_id(self, obj):
        return str(obj.id)[:8]
    short_id.short_description = "ID corto"