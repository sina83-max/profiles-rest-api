from django.urls import path, URLPattern

from . import views

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view())
]