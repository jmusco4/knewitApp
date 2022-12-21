from django.shortcuts import render
from django.views.generic import ListView
from .models import YourTests

class HomePageView(ListView):
    model = YourTests
    template_name = 'home.html'
