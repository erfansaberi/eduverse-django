# Generated by Django 4.1.3 on 2023-06-14 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_section_section_type_section_sec_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='sec_file',
            field=models.FileField(upload_to='files/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'rar', 'zip', 'MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
