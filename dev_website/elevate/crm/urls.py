from django.urls import path

from . import views

urlpatterns = [

    path("", views.homepage),
    path("register", views.register),
    path("register1", views.register1)
]
