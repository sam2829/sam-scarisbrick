from django.db import models
from technologies.models import Technology


class Project(models.Model):
    """
    class for the projects model
    """
    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=200)
    overview = models.TextField(max_length=500)
    github = models.URLField()
    live_site = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    technologies = models.ManyToManyField(Technology)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} for {self.summary}'
