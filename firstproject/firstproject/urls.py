"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,re_path	#new
from FirstApp import views;
from multipleviewsapp import views as v1;	##new-App views
from app1 import views as v11
from app2 import views as v22
from app1.views import f11
from app2.views import f22




urlpatterns = [
	
#MultiViewsApp as v1(alias to views.py)
	path('mrng/',v1.f1),
	path('aftr/',v1.f2),
	path('evng/',v1.f3),
    path('hello2/',v11.f11),
    path('datetime2/',v22.f22),
    path('hello3/',f11),
	path('datetime3/',f22),
    path('firstdemo/',views.demo),
	path('seconddemo/',views.demo),
	path('thirddemo/',views.demo),
    re_path("^.*$",views.homepage),



]; 

