from django.db import models


class Technology(models.Model):
    """
    class for the technology model, representing different
    languages, frameworks used etc
    """
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
