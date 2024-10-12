from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    """
    class for projects in the admin page
    """
    list_display = ('title', 'summary', 'created_at')
    search_fields = ('title', 'github', 'live_site', 'technologies')
    list_filter = ('technologies')

    def save_model(self, request, obj, form, change):
        # Validate the image before saving
        obj.clean()
        super().save_model(request, obj, form, change)

# Register the Project model with the ProjectAdmin configuration
admin.site.register(Project, ProjectAdmin)
