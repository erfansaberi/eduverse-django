from django.urls import path
from . import views


urlpatterns = [
    path('', views.CourseListView.as_view(), name='course-list'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('<slug:course_slug>/sections/', views.CourseSectionListView.as_view(), name='section-list'),
    path('<slug:course_slug>/sections/<int:section_idx>/', views.CourseSectionDetailView.as_view(), name='section-detail'),
]
