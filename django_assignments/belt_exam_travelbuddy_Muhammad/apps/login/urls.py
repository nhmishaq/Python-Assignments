from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^main/$', views.main),
    url(r'^travels/$', views.travels),
    url(r'^newuser/$', views.newuser),
    url(r'^success/(?P<id>[0-9]+)$', views.success),
    url(r'^login/$', views.login),
    url(r'^travels/destination/(?P<id>[0-9]+)', views.destination),
    url(r'^logout', views.logout),
    url(r'^process_trip', views.process_trip),
    url(r'^destination', views.destination),
    url(r'^add_trip', views.add_trip),
    url(r'^join/(?P<id>[0-9]+)$', views.join)



]