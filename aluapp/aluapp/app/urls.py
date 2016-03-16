from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^announcements/(?P<pk>\d+)/(?P<slug>[-.\w]+)/$', views.AnnouncementDetail.as_view(), name='announcement'),
    url(r'^document_requests/(?P<pk>\d+)/(?P<slug>[-.\w]+)/$', views.document_request_detail, name='document_request'),
    url(r'^document_types/download/(?P<doc_type_id>\d+)/$', views.download_all_doc_type, name='download_all_doc_type'),
    url(r'^document_types/download/(?P<doc_type_id>\d+)/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',
      views.download_today_doc_type, name='download_today_doc_type'),
    url(r'^document_types/download_doc_type_by_date_range/$', views.download_doc_type_by_date_range, name='download_doc_type_by_date_range'),
    url(r'^document_types/download_all/$', views.download_all, name='download_all'),
    url(r'^import_list/$', views.import_list, name='import_list'),
    url(r'^post_announcement/$', views.post_announcement, name='post_announcement'),
    url(r'^post_document_request/$', views.post_document_request, name='post_document_request'),
    url(r'^mail_staff/$', views.mail_staff, name='mail_staff'),
]
