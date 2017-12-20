from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^create/', views.create),
    url('^success/', views.success),
    url('^loginsuccess/', views.loginsuccess),
    url('^dashboard/', views.user_dashboard),
    url('^pokes/(?P<id>\d+)/$', views.poke)
]