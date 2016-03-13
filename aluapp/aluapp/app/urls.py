from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^announcements/(?P<pk>\d+)/(?P<slug>[-.\w]+)/$', views.AnnouncementDetail.as_view(), name='announcement'),
    url(r'^doc_requests/(?P<pk>\d+)/(?P<slug>[-.\w]+)/$', views.DocumentRequestDetail.as_view(), name='document_request'),
    url(r'^import_list/$', views.import_list, name='import_list'),
    url(r'^post_announcement/$', views.post_announcement, name='post_announcement'),
    url(r'^post_doc_request/$', views.post_doc_request, name='post_doc_request'),
]
