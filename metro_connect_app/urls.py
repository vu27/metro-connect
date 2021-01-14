from django.urls import path
from .views import home_view, submitted_form_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home_view, name="home"),
    path("submitted-form/", submitted_form_view, name="submitted-form"),
]