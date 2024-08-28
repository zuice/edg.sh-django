from django.urls import path

from urlshortener import views

urlpatterns = [
    path("", views.dashboard_view, name="index"),
    path("create", views.create_view, name="create"),
    path("<str:slug>", views.link_view, name="slug"),
]
