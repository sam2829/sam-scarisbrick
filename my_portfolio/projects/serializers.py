from rest_framework import serializers
from .models import Project
from django.conf import settings

class ProjectSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_image(self, obj):
        return f"{obj.image.url}"