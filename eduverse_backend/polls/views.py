from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated

from .pagination import DefaultPagination
from .models import Poll, PollOption, PollVote
from .serializers import PollSerializer, PollOptionSerializer, PollVoteSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.
class PollListView(generics.ListCreateAPIView):
    queryset = Poll.active.all()
    serializer_class = PollSerializer
    permission_classes = [IsAdminOrReadOnly,]
    pagination_class = DefaultPagination


class AllPollOptionListView(generics.ListCreateAPIView):
    queryset = PollOption.active.all()
    serializer_class = PollOptionSerializer
    permission_classes = [IsAdminOrReadOnly,]
    pagination_class = DefaultPagination


class AllPollVoteListView(generics.ListCreateAPIView):
    queryset = PollVote.active.all()
    serializer_class = PollVoteSerializer
    permission_classes = [IsAdminOrReadOnly,]
    pagination_class = DefaultPagination


class SpecificPollOptionListView(views.APIView):
    serializer = PollOption

    def setup(self, request, poll_id, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.poll = get_object_or_404(Poll, id=poll_id)

    def get(self, request, *args, **kwargs):
        options = PollOption.objects.filter(poll=self.poll)
        serializer = self.serializer(options, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs): # TODO: Check permissions
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificPollVoteListView(views.APIView):
    serializer = PollVote

    def setup(self, request, poll_id, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.poll = get_object_or_404(Poll, id=poll_id)

    def get(self, request, *args, **kwargs):
        options = PollVote.objects.filter(poll=self.poll)
        serializer = self.serializer(options, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO: If a user wants to vote to a poll, first, the user_voted method should be called and if the value is True, user must not be able to vote.
# TODO: If a user is not enrolled to a course, then he should not be able to vote to that poll
# TODO: If a poll due_date is passed, then recieving votes must be stopped for it