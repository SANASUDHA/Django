"""udacity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from courses import views as courses_views
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('mycourses/',include('courses.urls')),
    path('courses/',courses_views.home, name='home'),
    path('courses/details',courses_views.dummies, name='dummies'),
    path('courses/add',courses_views.addDummies, name='addDetails'),
    path('courses/edit/<int:dummy_id>',courses_views.editDummies, name='editDummies'),
    path('courses/delete/<int:dummy_id>',courses_views.deleteDummies, name='deleteDummies'),
    path("login/",auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path("logout/",auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),

    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile,name='profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
