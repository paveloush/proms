# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PromiseListView.as_view(), name='promise_list'),
    url(r'^(?P<pk>\d+)/$', views.PromiseDetailView.as_view(), name='promise_page'),

    url(r'^person$', views.PersonListView.as_view(), name='person_list'),
    url(r'^person/(?P<pk>\d+)/$', views.PersonDetailView.as_view(), name='person_page'),

]
