from django import views
from django.http import HttpResponse
from django.shortcuts import render
from views import views

# Create your views here.

class NewArticle(views):
    def get(self, request):
        return render (HttpResponse("This is a view"))
    def post(self, request):
        return HttpResponse("this is a simple message")