# Generated by Django 4.1.3 on 2023-06-11 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_managers_course_deleted_at_section_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('-course__id', '-index')},
        ),
        migrations.AlterField(
            model_name='section',
            name='index',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
