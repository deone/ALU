from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^announcements/(?P<slug>[-.\w]+)/$', views.AnnouncementDetail.as_view(), name='announcement'),
    url(r'^import_list/$', views.import_list, name='import_list'),
    url(r'^post_announcement/$', views.post_announcement, name='post_announcement'),
]
