from rest_framework import serializers
from .models import Poll, PollOption, PollVote

# TODO: Check the serializers
class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'
        

class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = '__all__'
        

class PollVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollVote
        fields = '__all__'
