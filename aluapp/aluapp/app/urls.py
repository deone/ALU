from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^announcements/(?P<pk>\d+)/(?P<slug>[-.\w]+)/$', views.AnnouncementDetail.as_view(), name='announcement'),
    url(r'^document_requests/(?P<pk>\d+)/(?P<slug>[-.\w]+)/$', views.document_request_detail, name='document_request'),
    url(r'^import_list/$', views.import_list, name='import_list'),
    url(r'^post_announcement/$', views.post_announcement, name='post_announcement'),
    url(r'^post_document_request/$', views.post_document_request, name='post_document_request'),
]
