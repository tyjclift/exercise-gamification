from django.urls import path, include

from . import views

# app_name = 'index'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("accounts/", include("allauth.urls")),
    path("upper/", views.UpperBodyView, name="upper"),
    path("cardio/", views.CardioView, name="cardio"),
    path("lower/", views.LowerBodyView, name="lower"),
]
