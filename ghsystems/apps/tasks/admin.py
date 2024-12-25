from django.contrib.admin import register as admin_register, ModelAdmin

from ghsystems.apps.tasks.models import Tasks


@admin_register(Tasks)
class TasksAdmin(ModelAdmin):
    """Tasks Admin for Admin Site."""
