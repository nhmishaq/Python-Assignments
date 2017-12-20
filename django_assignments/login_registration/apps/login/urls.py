from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^create/', views.create),
    url('^success/', views.success),
    url('^loginsuccess/', views.loginsuccess)
]