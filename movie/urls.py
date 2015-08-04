from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/search/$', views.search, name='search'),
    url(r'^/detail/(?P<imdbID>tt[0-9]+)$', views.detail, name="detail"),
]
