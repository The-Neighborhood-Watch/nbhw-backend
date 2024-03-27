from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("login", views.login),
    re_path("signup", views.signup),
    re_path("test_token", views.test_token),
    path("", RedirectView.as_view(url='/admin', permanent=False)),
]
