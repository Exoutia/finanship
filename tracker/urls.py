from django.urls import path
from tracker.views import home

urlpatterns = [
    path("", view=home, name="index"),
]
