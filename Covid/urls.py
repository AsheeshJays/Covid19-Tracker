from django.contrib import admin
from django.urls import path
from Covid import views

urlpatterns = [
    path('', views.index)
]