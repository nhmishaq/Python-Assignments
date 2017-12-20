from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^show_user$', views.show_user),
    url(r'^create_new$', views.create_new),
    # url(r'^edit_user$', views.edit_user),
]
