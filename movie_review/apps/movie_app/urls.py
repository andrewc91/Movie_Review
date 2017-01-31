from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new$', views.new, name="new"),
    url(r'^watch$', views.watch, name="watch"),
    url(r'^create$', views.create, name="create"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show"),
    url(r'^movie/(?P<id>\d+)$', views.showMovie, name="showMovie"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
    url(r'^create_review/(?P<id>\d+)$', views.create_review, name="create_review"),
    url(r'^add$', views.add, name="add"),
    url(r'^add_outing$', views.add_outing, name="add_outing"),
    url(r'^outing/(?P<id>\d+)$', views.outing, name="outing"),
    url(r'^outing/join/(?P<id>\d+)$', views.outing_join, name="outing_join"),
    url(r'^cancel/(?P<id>\d+)$', views.cancel, name="cancel"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete")
]
