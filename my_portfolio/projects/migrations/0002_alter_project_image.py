# Generated by Django 5.1.2 on 2024-10-12 13:40

import projects.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='', validators=[projects.models.validate_image]),
        ),
    ]
