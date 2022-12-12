from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView 
from .models import *
# Create your views here.
class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 3

class AboutPage(TemplateView):
    template_name = 'about.html'

class ContactPage(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = "__all__"

class My_teamPage(TemplateView):
    template_name = 'my_team.html'

class ReklamaPage(TemplateView):
    template_name = 'reklama.html'


