from rest_framework import serializers
from .models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    """
    class for technology model serializers
    """
    class Meta:
        model = Technology
        fields = ['name']