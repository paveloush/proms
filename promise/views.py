from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *

# Create your views here.


# Create your views here.
class PromiseListView(generic.ListView):
    template_name = 'promise/list_all.html'
    context_object_name = 'promise_list_all'

    def get_queryset(self):
        return Promise.objects.all().order_by('-id')


class PromiseDetailView(generic.DetailView):
    model = Promise
    template_name = 'promise/detail.html'
    context_object_name = 'promise'


class PersonListView(generic.ListView):
    template_name = 'person/list_all.html'
    context_object_name = 'person_list_all'

    def get_queryset(self):
        return Person.objects.all().order_by('-id')


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'person/detail.html'
    context_object_name = 'person'
