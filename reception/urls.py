from django.conf.urls import include, url, patterns
from . import views

urlpatterns = [
    url(r'^base/$', views.base, name='base'),
    url(r'^appointments/$', views.blank, name='appointments'),
    url(r'^ajax/$', views.ajax, name='ajax'),
]
