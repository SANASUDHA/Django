from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request,id):
	return HttpResponse("<h1>Welcome to Django</h1>"+id)

def home(request):
	return HttpResponse("<h3>Welcome to aboutPage</h3>")

def about(request):
	return HttpResponse("<h1>Welcome to Django</h1>")

def homePage(request):
	return render(request,"sample/home.html")


	