"""myapps2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from album import views


urlpatterns = [
    path('',views.first_view,name='Hola'),
    path('category',views.category,name='category-list'),
    path('category/<int:category_id>/detail', views.category_detail, name='category-detail'),
    path('photo/',views.PhotoListView.as_view()), 
    path('photo/<int:DetailView>/detail',views.PhotoDetailView, name='photo-detail'), 

]
