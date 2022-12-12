from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name = "home"),
    path('about/', AboutPage.as_view(), name = "about"),
    path('contact/', ContactPage.as_view(), name = "contact"),
    path('team/', My_teamPage.as_view(), name = "team"),
    path('reklama/', ReklamaPage.as_view(), name = 'reklama'),
]