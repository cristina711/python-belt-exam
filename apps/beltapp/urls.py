from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^friendprofile/(?P<friend_id>\d+)$', views.friendprofile),
    url(r'^othersprofile/(?P<other_id>\d+)$', views.othersprofile),
    url(r'^addfriend/(?P<other_id>\d+)$', views.addfriend),
    url(r'^removefriend/(?P<friend_id>\d+)$', views.removefriend),





    url(r'^logout$', views.logout),

]