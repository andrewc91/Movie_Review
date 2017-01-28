from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new$', views.new, name="new"),
    url(r'^watch$', views.watch, name="watch"),
    url(r'^create$', views.create, name="create"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show"),
    url(r'^movie/(?P<id>\d+)$', views.movie, name="movie"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
    url(r'^create_review/(?P<id>\d+)$', views.create_review, name="create_review")
]
