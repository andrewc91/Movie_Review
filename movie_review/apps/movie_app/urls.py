from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new$', views.new, name="new"),
    url(r'^watch$', views.watch, name="watch"),
    url(r'^create$', views.create, name="create"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show")
]
