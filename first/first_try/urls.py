from django.contrib import admin
from django.urls import path, include
from .views import show_site

urlpatterns = [
    path("", show_site)
]