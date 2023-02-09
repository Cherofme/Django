from django.shortcuts import render

# Create your views here.

def show_site(request):
    return render(request, "templates\first.html")