from django.contrib import admin
from .models import Technology


class TechnologyAdmin(admin.ModelAdmin):
    """
    class for technologies in the admin page
    """
    list_display = ('name')
    search_fields = ('name')
    list_filter = ('name')

# Register the Technology model with the Technology Admin configuration
admin.site.register(Technology, TechnologyAdmin)
