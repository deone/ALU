from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='topics'),
    url(r'^topics/(?P<slug>[-.\w]+)/$', views.index, name='topic'),
]
