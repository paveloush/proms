from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import generic

from promise.filters import PromiseFilter
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



def search(request):
    promise_list = Promise.objects.all()
    promise_filter = PromiseFilter(request.GET, queryset=promise_list)
    return render(request, 'search/promise_list.html', {'filter': promise_filter})