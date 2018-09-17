from django.urls import path

from Display.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="home")
]