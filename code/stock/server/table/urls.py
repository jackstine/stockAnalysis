from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tables', views.getTables,name='tables'),
    url(r'^$', views.test, name='index'),
]
