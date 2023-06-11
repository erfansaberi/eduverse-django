from rest_framework import serializers
from .models import Course, Section


class CourseSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'password': {'write_only': True}
        }