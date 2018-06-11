# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', PersonListView.as_view(), name='person_list'),
    url(r'^(?P<pk>\d+)/$', PersonDetailView.as_view(), name='person_page'),

]
