from django.contrib import admin
from .models import Poll, PollOption, PollVote


class PollOptionInline(admin.StackedInline): # TODO: Query optimization needed (if possible)
    model = PollOption
    fields = ('option','votes_count')
    readonly_fields = ('votes_count',)
    extra = 0
    min_num = 2
    max_num = 10
    

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('course', 'question', 'created_at', 'due_date')
    list_filter = ('course', 'created_at', 'due_date')
    search_fields = ('question',)
    inlines = [PollOptionInline]
    
@admin.register(PollVote)
class PollVoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'option', 'user', 'submitted_at')
    list_filter = ('poll', 'option', 'user')
    search_fields = ('poll', 'option', 'user')
    
    def get_queryset(self, request): # TODO: Check if this works
        return super().get_queryset(request)\
            .prefetch_related('user')\
            .prefetch_related('poll')\
            .prefetch_related('option')