from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated

from .pagination import DefaultPagination
from .models import Course, Section
from .serializers import CourseSerializer, CourseSectionsSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.active.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly,]
    pagination_class = DefaultPagination
    lookup_field = 'slug'


class LatestCourseListView(generics.ListCreateAPIView):
    queryset = Course.active.all().order_by('-created_at')
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly,]
    pagination_class = DefaultPagination
    lookup_field = 'slug'


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.active.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly,]
    lookup_field = 'slug'


class CourseSectionListView(views.APIView):
    serializer = CourseSectionsSerializer

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.course = get_object_or_404(Course, is_active=True, slug=course_slug)

    def get(self, request, course_slug):
        sections = Section.objects.filter(course=self.course)
        serializer = self.serializer(sections, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseSectionDetailView(views.APIView):
    serializer = CourseSectionsSerializer

    def get(self, request, course_slug, section_idx):
        course = get_object_or_404(Course, is_active=True, slug=course_slug)
        section = get_object_or_404(Section, course=course, index=section_idx)
        serializer = self.serializer(section)
        return Response(serializer.data)