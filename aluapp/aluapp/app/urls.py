from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^announcements/(?P<pk>\d+)/(?P<slug>[-.\w]+)/$', views.AnnouncementDetail.as_view(), name='announcement'),
    url(r'^document_requests/(?P<pk>\d+)/(?P<slug>[-.\w]+)/$', views.document_request_detail, name='document_request'),
    url(r'^document_types/download/(?P<doc_type_id>\d+)/$', views.download_all, name='document_type_download_all'),
    url(r'^document_types/download/(?P<doc_type_id>\d+)/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',
      views.download, name='document_type_download'),
    url(r'^import_list/$', views.import_list, name='import_list'),
    url(r'^post_announcement/$', views.post_announcement, name='post_announcement'),
    url(r'^post_document_request/$', views.post_document_request, name='post_document_request'),
]
