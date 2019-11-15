from django.urls import path
from .import views

urlpatterns = [
	path('',views.about, name='about'),
    path('<str:id>',views.home, name='home'),
    path('abc/<int:id>',views.home, name='home'),
    path("home/page",views.homePage)
]
