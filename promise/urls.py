# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.PromiseListView.as_view(), name='promise_list'),
    path('<int:promise_id>/', views.PromiseDetailView.as_view(), name='promise_page'),

    path('search/', views.search, name='search'),

]
