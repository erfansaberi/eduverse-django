from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Poll(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    
    def __str__(self):
        return f"[Poll {self.id}] {self.question}"
    
    def options(self):
        return PollOption.objects.filter(poll=self)
    
    def user_voted(self, user):
        return PollVote.objects.filter(poll=self, user=user).exists()


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.option}"
    
    def votes_count(self):
        return PollVote.objects.filter(poll=self.poll, option=self).count()


class PollVote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option = models.ForeignKey(PollOption, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)