from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sbi),
    path("index", views.index),
    path("create", views.create),
    path("search", views.search),
    path("update", views.update),
    path("delete", views.delete),
    path("all", views.Alllaptops),
    path("price", views.Price),
    path("between", views.between),
    path("account", views.account),
    path("deposit", views.deposit),
    path("withdraw", views.withdraw),
    path("details", views.details)

]
