# Generated by Django 4.2.2 on 2023-06-13 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_section_options_alter_section_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-updated_at', 'title')},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('-course__id', 'index')},
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('course', 'index')},
        ),
    ]
