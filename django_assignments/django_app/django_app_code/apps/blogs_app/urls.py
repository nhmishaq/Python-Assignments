from django.conf.urls import url
from . import views          
  
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new', views.new),
    url(r'^create', views.create),
    url(r'^show', views.show),
    url(r'^(?P<number>[0-9]{4})', views.show),
    url(r'^edit/(?P<year>[0-9]{4})', views.edit),
    url(r'^delete', views.destroy)
  ]