from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.users_new),
    url(r'^(?P<userid>[0-9]{2})/edit', views.edit),
    url(r'^(?P<userid>[0-9]{2}$)', views.show),
    url(r'create$', views.create),
    url(r'^(?P<userid>[0-9]{2})/destroy', views.destroy),
    url(r'^update/(?P<userid>[0-9]{2})', views.update),
]