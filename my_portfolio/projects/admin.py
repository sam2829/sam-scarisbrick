from django.contrib import admin
from django import forms
from .models import Project
from django.contrib.admin.widgets import FilteredSelectMultiple


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'technologies': FilteredSelectMultiple("Technologies", is_stacked=False),
        }



class ProjectAdmin(admin.ModelAdmin):
    """
    class for projects in the admin page
    """
    form = ProjectAdminForm
    list_display = ('title', 'summary', 'created_at')
    search_fields = ('title', 'github', 'live_site', 'technologies')
    list_filter = ['technologies']

    def save_model(self, request, obj, form, change):
        # Validate the image before saving
        obj.clean()
        super().save_model(request, obj, form, change)

# Register the Project model with the ProjectAdmin configuration
admin.site.register(Project, ProjectAdmin)
