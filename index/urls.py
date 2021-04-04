from django.urls import path, include

from . import views

# app_name = 'index'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("accounts/", include("allauth.urls")),
   # path("cardio/", views.CardioView.as_view(), name="cardio"),
   # path("lower/", views.LowerBodyView.as_view(), name="lower"),
   # path("upper/", views.UpperBodyView.as_view(), name="upper"),
    path("upper/", views.UpperBodyView, name="upper"),
    path("cardio/", views.CardioView, name="cardio"),
    path("lower/", views.LowerBodyView, name="cardio"),
]
