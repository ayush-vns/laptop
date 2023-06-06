from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sbi),
    path("index", views.index),
    path("account", views.account),
    path("deposit", views.deposit),
    path("withdraw", views.withdraw),
    path("details", views.details),
    

]
