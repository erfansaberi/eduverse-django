import datetime
from django.db.models import Manager



class ActivePollsManager(Manager):
    def get_queryset(self): # TODO: Check This
        return super().get_queryset().filter(due_date__gt=datetime.datetime.now())
