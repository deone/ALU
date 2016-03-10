from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^import_list/$', views.import_list, name='import_list'),
]
