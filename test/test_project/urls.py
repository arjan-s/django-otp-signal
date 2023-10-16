from django.urls import re_path
from django.contrib import admin
import django.contrib.auth.views


urlpatterns = [
    re_path(r'^login/$', django.contrib.auth.views.LoginView.as_view()),
    re_path(r'^logout/$', django.contrib.auth.views.LogoutView.as_view()),
    re_path(r'^admin/', admin.site.urls),
]
