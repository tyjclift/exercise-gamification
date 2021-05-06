from django.urls import path, include

from . import views

#app_name = "index"

# REFERENCES
# Title: Django-allauth
# URL: https://django-allauth.readthedocs.io/en/latest/installation.html
# Software License: MIT License

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("accounts/", include("allauth.urls")),
    path("upper/", views.UpperBodyView, name="upper"),
    path("cardio/", views.CardioView, name="cardio"),
    path("lower/", views.LowerBodyView, name="lower"),
    path('social/', views.SocialView, name="social"),
    path('friendship',include("friendship.urls")),
    path("database_list/", views.UserListView, name="database_list")
]
