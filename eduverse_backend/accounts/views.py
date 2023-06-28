from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from .models import Student

# Create your views here.
class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.POST)
        if serializer.is_valid():
            user = User.objects.create_user(
                username = serializer.validated_data['username'],
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password']
            )
            Student.objects.create(user=user, student_id=serializer.validated_data['student_id'])
            return Response(serializer.data)
        return Response(serializer.errors)