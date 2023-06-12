from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from .managers import ActiveCoursesManager

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    en_title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images/%Y/%m/%d/')
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    active = ActiveCoursesManager()

    class Meta:
        ordering = ('-updated_at', 'title')
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.en_title)
        super().save(*args, **kwargs)


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    index = models.PositiveSmallIntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    # temp
    section_type = models.CharField(max_length=100)

    class Meta:
        ordering = ('-course__id', 'index')
        indexes = [
            models.Index(fields=['-created_at'])
        ]
        unique_together = ('course', 'index')

    def __str__(self):
        return f'{self.course} - {self.title}'
