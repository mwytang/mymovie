from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^save/(?P<imdbID>tt[0-9]+)$', views.save, name='save'),
]
