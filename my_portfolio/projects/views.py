from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from .filters import ProjectFilter

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # Use the filter set created
    filterset_class = ProjectFilter
    # Add the filter backend
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)