from django.shortcuts import render
from django.views.generic import ListView, DetailView



from .models import Product



class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'













