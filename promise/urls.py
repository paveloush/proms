# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PromiseListView.as_view(), name='promise_list'),
    url(r'^(?P<pk>\d+)/$', views.PromiseDetailView.as_view(), name='promise_page'),

]
