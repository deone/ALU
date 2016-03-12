from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='topics'),
    url(r'^topics/(?P<pk>\d+)/(?P<slug>[-.\w]+)/$', views.TopicDetail.as_view(), name='topic'),
]
