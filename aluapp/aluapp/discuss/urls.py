from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='topics'),
    url(r'^topics/new/$', views.new_topic, name='new_topic'),
    url(r'^topics/(?P<pk>\d+)/(?P<slug>[-.\w]+)/$', views.topic_detail, name='topic'),
]
