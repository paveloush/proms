from django.shortcuts import render
from django.views import generic
from .models import Person


# Create your views here.



class PersonListView(generic.ListView):
    template_name = 'person/list_all.html'
    context_object_name = 'person_list_all'

    def get_queryset(self):
        return Person.objects.all().order_by('-id')


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'person/detail.html'
    context_object_name = 'person'
