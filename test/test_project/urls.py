import django.contrib.auth.views
from django.contrib import admin
from django.urls import re_path

urlpatterns = [
    re_path(r"^login/$", django.contrib.auth.views.LoginView.as_view()),
    re_path(r"^logout/$", django.contrib.auth.views.LogoutView.as_view()),
    re_path(r"^admin/", admin.site.urls),
]
