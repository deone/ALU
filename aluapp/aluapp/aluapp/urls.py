from django.conf.urls import url, include
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^app/', include('app.urls', namespace='app')),
    url(r'^admin/', admin.site.urls),
]
