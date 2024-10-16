from rest_framework import serializers
from .models import Project
from technologies.serializers import TechnologySerializer

class ProjectSerializer(serializers.ModelSerializer):
    """
    class for project model serializers
    """
    image = serializers.SerializerMethodField()
    technologies = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    # Get the image field url
    def get_image(self, obj):
        return f"{obj.image.url}"
    
    # create the technologies into one array
    def get_technologies(self, obj):
        return [tech.name for tech in obj.technologies.all()] 