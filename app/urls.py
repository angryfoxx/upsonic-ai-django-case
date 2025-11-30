from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_number, name="show_number"),
]
