from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
class IndexUser(View):
    def get(self, requests):
        return HttpResponse("Hello World USERS")