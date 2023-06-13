from django.contrib import admin
from .models import Poll, PollOption, PollVote


class PollOptionInline(admin.StackedInline):
    model = PollOption
    list_display = ('option', 'votes_count')
    extra = 2
    min_num = 2
    max_num = 10

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('course', 'question', 'created_at', 'due_date')
    list_filter = ('course', 'created_at', 'due_date')
    search_fields = ('question',)
    inlines = [PollOptionInline]
    # TODO: Select poll options in the same page when adding poll (inline)
    
@admin.register(PollVote)
class PollVoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'option', 'user', 'submitted_at') # TODO: Query prefetch user and poll
    list_filter = ('poll', 'option', 'user')
    search_fields = ('poll', 'option', 'user')