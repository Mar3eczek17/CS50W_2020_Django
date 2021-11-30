from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("marek", views.marek, name="marek"),
    path("david", views.david, name="david")
]
