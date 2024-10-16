from django.db import models
from technologies.models import Technology
from django.core.exceptions import ValidationError  # Import ValidationError
from django.core.files.images import get_image_dimensions
from cloudinary.models import CloudinaryField
import os


def validate_image(file):
    # If no new file is being uploaded, skip validation
    if not hasattr(file, 'file') or not file.file:
        return
    if hasattr(file, 'url'):
        # Extract the file extension from the Cloudinary URL
        extension = os.path.splitext(file.url)[-1].lower().replace('.', '')
    else:
        # Fallback for local files
        extension = os.path.splitext(file.name)[-1].lower().replace('.', '')
    # Ensure the file is an image
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
   
    if extension not in valid_extensions:
        raise ValidationError(
            f"Unsupported file extension. Allowed extensions are "
            f"{valid_extensions}"
        )

        # Optionally, check the image dimensions
    try:
        # Check the file size (10MB maximum)
        filesize = file.size
        max_filesize = 10 * 1024 * 1024  # 10MB in bytes
        if filesize > max_filesize:
            raise ValidationError(
                "The maximum file size that can be uploaded is 10MB."
            )
        width, height = get_image_dimensions(file)
        max_dimension = 4096
        if width > max_dimension or height > max_dimension:
            raise ValidationError(
                f"Image dimensions are too large. Maximum width and height"
                f" allowed is {max_dimension}px."
            )
    except AttributeError:
        raise ValidationError("Invalid image file.")


class Project(models.Model):
    """
    class for the projects model
    """
    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=200)
    overview = models.TextField(max_length=500)
    image = CloudinaryField('images', blank=False, validators=[validate_image])
    github = models.URLField()
    live_site = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    technologies = models.ManyToManyField(Technology)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} for {self.summary}'
