from django.contrib import admin
from .models import Course, Section

# Register your models here.
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'course', 'created_at')
    ordering = ('-course__id', '-index')
    raw_id_fields = ('course',)


class SectionInline(admin.TabularInline):
    model = Section


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline,]
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at', 'title')
    prepopulated_fields = {'slug': ('en_title',)}
    date_hierarchy = 'created_at'