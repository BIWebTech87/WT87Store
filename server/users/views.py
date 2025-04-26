from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, permissions
from .models import User

from .serializers import UserSerializer


# Create your views here.
class IndexUser(View):
    def get(self, requests):
        return HttpResponse("Hello World USERS")

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permision_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'patch', 'delete']